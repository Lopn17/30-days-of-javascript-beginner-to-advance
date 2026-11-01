"""
SnapSort: The Speed Sorting Challenge (versi Pygame)

Kontrol:
  Mouse : klik angka pertama, lalu klik angka kedua -> keduanya tukar posisi
  Keyboard: <- / -> pindah kursor, SPACE pilih / tukar
  ENTER   : cek susunan
  R       : ronde baru
  1/2/3   : ganti difficulty (otomatis ronde baru)
  ESC     : keluar

Prinsip desain (sesuai "Developer Mindset" Day 3):
  - DATA (list Tile) adalah satu-satunya sumber kebenaran.
  - Tampilan hanya dirender dari data itu.
  - Validasi membandingkan NILAI, bukan identitas tile -> aman untuk angka duplikat.
  - Skor hanya bisa diberikan sekali per ronde lewat state machine.
"""
import os
import random
import sys

import pygame

W, H = 900, 600
FPS = 60

DIFFICULTIES = {
    1: {"name": "EASY",   "count": 5,  "time": 40, "max": 20},
    2: {"name": "MEDIUM", "count": 7,  "time": 35, "max": 15},   # max kecil -> duplikat sering muncul
    3: {"name": "HARD",   "count": 10, "time": 30, "max": 12},
}

# warna
BG = (14, 16, 28)
PANEL = (26, 30, 52)
TILE = (60, 90, 200)
TILE_SEL = (255, 190, 60)
TILE_CUR = (120, 220, 255)
TEXT = (235, 238, 250)
DIM = (140, 148, 180)
GOOD = (80, 220, 130)
BAD = (240, 90, 90)

# state ronde
PLAYING, WON, LOST = "PLAYING", "WON", "LOST"


class Tile:
    """Satu angka di board. x/target_x hanya untuk animasi, bukan data game."""

    def __init__(self, value):
        self.value = value
        self.x = 0.0
        self.target_x = 0.0


class Game:
    def __init__(self):
        self.level = 2
        self.total_score = 0
        self.combo = 0
        self.best_time = {}          # {level: detik tercepat}, hanya selama sesi
        self.msg = ""
        self.msg_color = TEXT
        self.shake = 0.0
        self.new_round()

    # ---------- ronde ----------
    def new_round(self):
        cfg = DIFFICULTIES[self.level]
        self.count = cfg["count"]
        self.time_limit = float(cfg["time"])
        self.time_left = self.time_limit
        self.state = PLAYING
        self.round_score = 0          # skor ronde ini
        self.score_awarded = False    # guard: skor hanya boleh dihitung sekali
        self.selected = None          # index tile yang dipilih
        self.cursor = 0               # kursor keyboard
        self.checks = 0
        self.shake = 0.0

        # generate angka acak; ulangi kalau kebetulan sudah terurut
        while True:
            values = [random.randint(1, cfg["max"]) for _ in range(self.count)]
            if values != sorted(values):
                break
        self.tiles = [Tile(v) for v in values]
        self.layout(snap=True)
        self.set_msg("Urutkan dari kecil ke besar!", TEXT)

    def set_msg(self, text, color):
        self.msg, self.msg_color = text, color

    # ---------- layout ----------
    def layout(self, snap=False):
        gap = 12
        tw = min(90, (W - 100 - gap * (self.count - 1)) // self.count)
        self.tw = tw
        total = tw * self.count + gap * (self.count - 1)
        start = (W - total) // 2
        for i, t in enumerate(self.tiles):
            t.target_x = start + i * (tw + gap)
            if snap:
                t.x = t.target_x

    def tile_rect(self, i):
        t = self.tiles[i]
        y = 250
        off = 0
        if self.shake > 0:
            off = random.randint(-6, 6)
        return pygame.Rect(int(t.x) + off, y, self.tw, self.tw)

    # ---------- aksi pemain ----------
    def pick(self, i):
        """Dipanggil mouse/keyboard. Pilih tile atau tukar dengan tile terpilih."""
        if self.state != PLAYING:
            return
        if self.selected is None:
            self.selected = i
        elif self.selected == i:
            self.selected = None
        else:
            j = self.selected
            self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]  # tukar DATA
            self.selected = None
            self.layout()                                                # animasi menyusul data

    def values(self):
        return [t.value for t in self.tiles]

    def check(self):
        if self.state != PLAYING:      # cek berulang setelah ronde selesai diabaikan
            return
        self.checks += 1
        vals = self.values()
        target = sorted(vals)
        if vals == target:             # bandingkan nilai -> duplikat aman
            self.win()
        else:
            correct = sum(1 for a, b in zip(vals, target) if a == b)
            self.shake = 0.3
            self.time_left = max(0.0, self.time_left - 2.0)   # penalti waktu
            self.set_msg(f"Belum benar: {correct}/{self.count} posisi tepat (-2 detik)", BAD)

    def win(self):
        self.state = WON
        self.combo += 1
        used = self.time_limit - self.time_left
        base = self.count * 100
        time_bonus = int(self.time_left * 10)
        combo_bonus = (self.combo - 1) * 50
        penalty = (self.checks - 1) * 25
        self.award(max(0, base + time_bonus + combo_bonus - penalty))
        lvl = self.level
        if lvl not in self.best_time or used < self.best_time[lvl]:
            self.best_time[lvl] = used
        self.set_msg(f"BENAR! +{self.round_score}  (combo x{self.combo})  |  R = ronde baru", GOOD)

    def lose(self):
        self.state = LOST
        self.combo = 0
        self.set_msg("WAKTU HABIS!  |  R = ronde baru", BAD)

    def award(self, pts):
        """Satu-satunya tempat skor bertambah, dijaga flag agar tidak double."""
        if self.score_awarded:
            return
        self.score_awarded = True
        self.round_score = pts
        self.total_score += pts

    # ---------- update ----------
    def update(self, dt):
        if self.state == PLAYING:
            self.time_left -= dt
            if self.time_left <= 0:
                self.time_left = 0
                self.lose()
        if self.shake > 0:
            self.shake -= dt
        k = min(1.0, 14 * dt)
        for t in self.tiles:
            t.x += (t.target_x - t.x) * k

    # ---------- render ----------
    def draw(self, screen, fonts):
        screen.fill(BG)
        big, mid, small = fonts

        title = big.render("SNAPSORT", True, TILE_CUR)
        screen.blit(title, (W // 2 - title.get_width() // 2, 24))
        cfg = DIFFICULTIES[self.level]
        sub = small.render(f"Level: {cfg['name']}   [1][2][3] ganti level", True, DIM)
        screen.blit(sub, (W // 2 - sub.get_width() // 2, 90))

        # panel statistik
        pygame.draw.rect(screen, PANEL, (40, 130, W - 80, 70), border_radius=10)
        low = self.time_left <= 10 and self.state == PLAYING
        stats = [
            ("WAKTU", f"{self.time_left:4.1f}s", BAD if low else TEXT),
            ("SKOR", str(self.total_score), TEXT),
            ("COMBO", f"x{self.combo}", TEXT),
            ("BEST", f"{self.best_time[self.level]:.1f}s" if self.level in self.best_time else "-", TEXT),
        ]
        for i, (label, val, col) in enumerate(stats):
            cx = 40 + (W - 80) * (i * 2 + 1) // 8
            l = small.render(label, True, DIM)
            v = mid.render(val, True, col)
            screen.blit(l, (cx - l.get_width() // 2, 138))
            screen.blit(v, (cx - v.get_width() // 2, 160))

        # bar waktu
        ratio = self.time_left / self.time_limit
        pygame.draw.rect(screen, PANEL, (40, 210, W - 80, 10), border_radius=5)
        pygame.draw.rect(screen, BAD if low else GOOD, (40, 210, int((W - 80) * ratio), 10), border_radius=5)

        # tile (dirender dari self.tiles)
        for i in range(self.count):
            r = self.tile_rect(i)
            color = TILE
            if self.selected == i:
                color = TILE_SEL
            pygame.draw.rect(screen, color, r, border_radius=12)
            if self.cursor == i and self.state == PLAYING:
                pygame.draw.rect(screen, TILE_CUR, r.inflate(8, 8), width=3, border_radius=14)
            txt = mid.render(str(self.tiles[i].value), True, (10, 12, 24) if self.selected == i else TEXT)
            screen.blit(txt, txt.get_rect(center=r.center))

        # pesan
        m = mid.render(self.msg, True, self.msg_color)
        screen.blit(m, (W // 2 - m.get_width() // 2, 380))

        # tombol
        self.btn_check = pygame.Rect(W // 2 - 220, 450, 200, 54)
        self.btn_new = pygame.Rect(W // 2 + 20, 450, 200, 54)
        active = self.state == PLAYING
        pygame.draw.rect(screen, TILE if active else (50, 54, 80), self.btn_check, border_radius=10)
        pygame.draw.rect(screen, (200, 90, 60), self.btn_new, border_radius=10)
        for rect, label in ((self.btn_check, "CEK (Enter)"), (self.btn_new, "BARU (R)")):
            s = mid.render(label, True, TEXT)
            screen.blit(s, s.get_rect(center=rect.center))

        hint = small.render("Klik / SPACE: pilih lalu tukar  |  Panah: gerak kursor", True, DIM)
        screen.blit(hint, (W // 2 - hint.get_width() // 2, 540))


def main():
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("SnapSort")
    clock = pygame.time.Clock()
    names = "consolas,menlo,dejavusansmono,monospace"
    fonts = (
        pygame.font.SysFont(names, 44, bold=True),
        pygame.font.SysFont(names, 28, bold=True),
        pygame.font.SysFont(names, 16),
    )
    game = Game()
    game.draw(screen, fonts)  # inisialisasi rect tombol

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                elif e.key == pygame.K_r:
                    game.new_round()
                elif e.key in (pygame.K_1, pygame.K_2, pygame.K_3):
                    game.level = {pygame.K_1: 1, pygame.K_2: 2, pygame.K_3: 3}[e.key]
                    game.combo = 0
                    game.new_round()
                elif e.key == pygame.K_LEFT:
                    game.cursor = (game.cursor - 1) % game.count
                elif e.key == pygame.K_RIGHT:
                    game.cursor = (game.cursor + 1) % game.count
                elif e.key == pygame.K_SPACE:
                    game.pick(game.cursor)
                elif e.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    game.check()
            elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if game.btn_check.collidepoint(e.pos):
                    game.check()
                elif game.btn_new.collidepoint(e.pos):
                    game.new_round()
                else:
                    for i in range(game.count):
                        if game.tile_rect(i).collidepoint(e.pos):
                            game.cursor = i
                            game.pick(i)
                            break

        game.update(dt)
        game.draw(screen, fonts)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()