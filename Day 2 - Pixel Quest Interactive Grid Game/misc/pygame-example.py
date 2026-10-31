'''
This Pygame is just an example of how the 
game works and looks like if you confused about the game.
the code was made with python, this is not a cheat sheet.
you need to figured out by yourself how to make the game
using html css and js. you may use this as refference instead 
of cheat sheet
'''
 
import random
import sys
import pygame

# Pixel Quest — Day 2
# Install: python -m pip install pygame
# Run:     python pixel_quest.py

pygame.init()

# ---------------------------- Configuration ----------------------------
WIDTH, HEIGHT = 1000, 760
FPS = 60
GRID_SIZE = 5
TOTAL_TILES = GRID_SIZE * GRID_SIZE
MAX_ATTEMPTS = 8
TILE_SIZE = 88
TILE_GAP = 10
GRID_PIXEL_SIZE = GRID_SIZE * TILE_SIZE + (GRID_SIZE - 1) * TILE_GAP

BG = (10, 14, 31)
PANEL = (19, 26, 51)
PANEL_LIGHT = (27, 36, 67)
TILE = (25, 38, 70)
TILE_HOVER = (36, 58, 98)
BORDER = (57, 79, 125)
CYAN = (64, 225, 255)
CYAN_DARK = (28, 126, 163)
PURPLE = (151, 105, 255)
GOLD = (255, 205, 82)
RED = (255, 91, 117)
GREEN = (89, 239, 177)
WHITE = (238, 244, 255)
MUTED = (145, 161, 196)
DARK = (8, 12, 26)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PIXEL QUEST — Find the Hidden Core")
clock = pygame.time.Clock()

# Use common system fonts so the game works on most computers.
font_title = pygame.font.SysFont("consolas", 38, bold=True)
font_heading = pygame.font.SysFont("consolas", 22, bold=True)
font_body = pygame.font.SysFont("consolas", 17)
font_small = pygame.font.SysFont("consolas", 14)
font_tiny = pygame.font.SysFont("consolas", 12, bold=True)

GRID_X = 72
GRID_Y = 205
SIDE_X = 625
SIDE_Y = 205
SIDE_W = 305
SIDE_H = 440
RESTART_RECT = pygame.Rect(SIDE_X + 22, SIDE_Y + SIDE_H - 76, SIDE_W - 44, 48)


def draw_text(surface, text, font, color, x, y, center=False):
    image = font.render(text, True, color)
    rect = image.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    surface.blit(image, rect)
    return rect


def panel(surface, rect, fill=PANEL, border=BORDER, radius=12, width=2):
    pygame.draw.rect(surface, fill, rect, border_radius=radius)
    pygame.draw.rect(surface, border, rect, width=width, border_radius=radius)


def draw_core(surface, center, size, color=GOLD):
    """Draw a small pixel-inspired glowing core using simple geometric shapes."""
    x, y = center
    glow = pygame.Surface((size * 3, size * 3), pygame.SRCALPHA)
    pygame.draw.rect(
        glow, (*color, 30),
        (size // 2, size // 2, size * 2, size * 2), border_radius=5
    )
    surface.blit(glow, (x - glow.get_width() // 2, y - glow.get_height() // 2))
    outer = [
        (x, y - size), (x + size // 2, y - size // 2),
        (x + size, y), (x + size // 2, y + size // 2),
        (x, y + size), (x - size // 2, y + size // 2),
        (x - size, y), (x - size // 2, y - size // 2)
    ]
    pygame.draw.polygon(surface, color, outer)
    pygame.draw.polygon(surface, WHITE, outer, width=2)
    pygame.draw.rect(surface, WHITE, (x - 3, y - 3, 6, 6))


class PixelQuest:
    def __init__(self):
        self.new_game()

    def new_game(self):
        # The target is chosen exactly once per run and never moves mid-game.
        self.target_index = random.randrange(TOTAL_TILES)
        self.revealed = {}  # tile index -> "miss" or "target"
        self.attempts_left = MAX_ATTEMPTS
        self.score = 0
        self.game_over = False
        self.won = False
        self.status = "SCAN THE GRID. FIND THE HIDDEN CORE."
        self.status_color = CYAN
        self.last_action = "NEW RUN INITIALIZED"
        self.hovered_tile = None

    def tile_rect(self, index):
        row, col = divmod(index, GRID_SIZE)
        return pygame.Rect(
            GRID_X + col * (TILE_SIZE + TILE_GAP),
            GRID_Y + row * (TILE_SIZE + TILE_GAP),
            TILE_SIZE, TILE_SIZE
        )

    def handle_tile_click(self, index):
        # Guard clauses keep the state consistent for repeated/late clicks.
        if self.game_over or index in self.revealed:
            return

        self.attempts_left -= 1

        if index == self.target_index:
            self.revealed[index] = "target"
            self.won = True
            self.game_over = True
            self.score += 100 + self.attempts_left * 10
            self.status = "CORE FOUND! MISSION COMPLETE."
            self.status_color = GREEN
            self.last_action = "TARGET ACQUIRED  //  +" + str(100 + self.attempts_left * 10) + " PTS"
        else:
            self.revealed[index] = "miss"
            self.score = max(0, self.score - 10)
            self.last_action = "EMPTY SECTOR  //  -10 PTS"
            if self.attempts_left <= 0:
                self.game_over = True
                self.won = False
                self.status = "SIGNAL LOST. THE CORE WAS HERE:"
                self.status_color = RED
                self.revealed[self.target_index] = "target"
            else:
                self.status = random.choice([
                    "NO SIGNAL HERE. KEEP SEARCHING.",
                    "EMPTY SECTOR. TRY ANOTHER TILE.",
                    "SCANNER CLEAR. TARGET STILL HIDDEN.",
                ])
                self.status_color = MUTED

    def handle_click(self, pos):
        if RESTART_RECT.collidepoint(pos):
            self.new_game()
            return

        if self.game_over:
            return

        for index in range(TOTAL_TILES):
            if self.tile_rect(index).collidepoint(pos):
                self.handle_tile_click(index)
                return

    def draw_background(self):
        screen.fill(BG)
        # Subtle sci-fi grid lines.
        for x in range(0, WIDTH, 40):
            pygame.draw.line(screen, (15, 22, 44), (x, 0), (x, HEIGHT), 1)
        for y in range(0, HEIGHT, 40):
            pygame.draw.line(screen, (15, 22, 44), (0, y), (WIDTH, y), 1)
        # Decorative corner lights.
        pygame.draw.circle(screen, CYAN_DARK, (24, 24), 3)
        pygame.draw.circle(screen, PURPLE, (WIDTH - 24, 24), 3)

    def draw_header(self):
        draw_text(screen, "PIXEL", font_title, WHITE, 54, 32)
        title_width = font_title.size("PIXEL")[0]
        draw_text(screen, "QUEST", font_title, CYAN, 54 + title_width + 8, 32)
        draw_text(screen, "FIND THE HIDDEN CORE", font_small, MUTED, 57, 79)
        draw_text(screen, "DAY 02  /  INTERACTIVE GRID SYSTEM", font_small, PURPLE, 57, 104)

        # Decorative signal bars.
        for i, h in enumerate([12, 20, 15, 27, 18, 31, 22]):
            pygame.draw.rect(screen, CYAN_DARK if i < 5 else PANEL_LIGHT,
                             (WIDTH - 170 + i * 14, 47 + (31 - h), 7, h), border_radius=2)
        draw_text(screen, "SIGNAL: ACTIVE", font_tiny, GREEN, WIDTH - 170, 86)

        pygame.draw.line(screen, BORDER, (54, 145), (WIDTH - 54, 145), 1)

    def draw_grid(self):
        draw_text(screen, "SEARCH SECTORS", font_heading, WHITE, GRID_X, 164)
        draw_text(screen, "SELECT A TILE TO SCAN", font_small, MUTED, GRID_X, 184)

        self.hovered_tile = None
        mouse_pos = pygame.mouse.get_pos()
        for index in range(TOTAL_TILES):
            rect = self.tile_rect(index)
            state = self.revealed.get(index)

            if rect.collidepoint(mouse_pos) and not self.game_over and index not in self.revealed:
                self.hovered_tile = index
                fill = TILE_HOVER
                outline = CYAN
            else:
                fill = TILE
                outline = BORDER

            if state == "miss":
                fill = (33, 29, 54)
                outline = (103, 65, 106)
            elif state == "target":
                fill = (62, 49, 27)
                outline = GOLD

            pygame.draw.rect(screen, fill, rect, border_radius=8)
            pygame.draw.rect(screen, outline, rect, width=2, border_radius=8)

            if state == "miss":
                cx, cy = rect.center
                pygame.draw.line(screen, RED, (cx - 10, cy - 10), (cx + 10, cy + 10), 3)
                pygame.draw.line(screen, RED, (cx + 10, cy - 10), (cx - 10, cy + 10), 3)
                draw_text(screen, "EMPTY", font_tiny, MUTED, cx, rect.bottom - 17, center=True)
            elif state == "target":
                draw_core(screen, rect.center, 17)
                draw_text(screen, "CORE", font_tiny, GOLD, rect.centerx, rect.bottom - 17, center=True)
            else:
                # Small tile ID and center pixel marker.
                row, col = divmod(index, GRID_SIZE)
                draw_text(screen, f"{row + 1}-{col + 1}", font_tiny, MUTED,
                          rect.x + 8, rect.y + 7)
                cx, cy = rect.center
                pygame.draw.rect(screen, CYAN_DARK, (cx - 3, cy - 3, 6, 6))

        if self.game_over and not self.won:
            # If the player loses, the target is revealed so the run has closure.
            pass

    def draw_side_panel(self):
        rect = pygame.Rect(SIDE_X, SIDE_Y, SIDE_W, SIDE_H)
        panel(screen, rect)
        draw_text(screen, "MISSION STATUS", font_heading, WHITE, SIDE_X + 22, SIDE_Y + 20)
        draw_text(screen, "RUN ID  //  PQ-02", font_small, MUTED, SIDE_X + 22, SIDE_Y + 51)
        pygame.draw.line(screen, BORDER, (SIDE_X + 22, SIDE_Y + 78),
                         (SIDE_X + SIDE_W - 22, SIDE_Y + 78), 1)

        draw_text(screen, "SCORE", font_small, MUTED, SIDE_X + 22, SIDE_Y + 98)
        draw_text(screen, f"{self.score:03d}", font_title, CYAN, SIDE_X + 22, SIDE_Y + 119)
        draw_text(screen, "PTS", font_small, MUTED, SIDE_X + 140, SIDE_Y + 143)

        draw_text(screen, "ATTEMPTS LEFT", font_small, MUTED, SIDE_X + 22, SIDE_Y + 190)
        draw_text(screen, f"{self.attempts_left:02d} / {MAX_ATTEMPTS:02d}",
                  font_heading, WHITE, SIDE_X + 22, SIDE_Y + 213)

        # Attempts progress bar.
        bar = pygame.Rect(SIDE_X + 22, SIDE_Y + 248, SIDE_W - 44, 10)
        pygame.draw.rect(screen, (8, 13, 29), bar, border_radius=5)
        ratio = self.attempts_left / MAX_ATTEMPTS
        bar_color = GREEN if ratio > 0.5 else GOLD if ratio > 0.25 else RED
        if self.attempts_left > 0:
            pygame.draw.rect(screen, bar_color,
                             (bar.x, bar.y, int(bar.width * ratio), bar.height), border_radius=5)

        draw_text(screen, "RULES", font_heading, WHITE, SIDE_X + 22, SIDE_Y + 278)
        draw_text(screen, "01  One tile = one attempt", font_small, MUTED, SIDE_X + 22, SIDE_Y + 310)
        draw_text(screen, "02  No repeat scans", font_small, MUTED, SIDE_X + 22, SIDE_Y + 334)
        draw_text(screen, "03  Find the core to win", font_small, MUTED, SIDE_X + 22, SIDE_Y + 358)

        button_fill = (33, 56, 88) if RESTART_RECT.collidepoint(pygame.mouse.get_pos()) else (24, 42, 70)
        button_border = CYAN if RESTART_RECT.collidepoint(pygame.mouse.get_pos()) else CYAN_DARK
        pygame.draw.rect(screen, button_fill, RESTART_RECT, border_radius=8)
        pygame.draw.rect(screen, button_border, RESTART_RECT, width=2, border_radius=8)
        draw_text(screen, "↻", font_heading, CYAN, RESTART_RECT.x + 18, RESTART_RECT.y + 10)
        draw_text(screen, "RESTART RUN", font_body, WHITE,
                  RESTART_RECT.centerx + 12, RESTART_RECT.centery, center=True)

    def draw_footer(self):
        footer = pygame.Rect(54, 680, WIDTH - 108, 48)
        panel(screen, footer, fill=(14, 20, 40), border=(36, 53, 88), radius=8, width=1)
        pygame.draw.circle(screen, self.status_color, (footer.x + 20, footer.centery), 5)
        draw_text(screen, self.status, font_small, self.status_color, footer.x + 36, footer.y + 8)
        draw_text(screen, self.last_action, font_tiny, MUTED, footer.x + 36, footer.y + 27)

        if self.game_over:
            label = "VICTORY" if self.won else "MISSION FAILED"
            color = GREEN if self.won else RED
            draw_text(screen, label, font_tiny, color, footer.right - 18, footer.centery, center=True)

    def draw(self):
        self.draw_background()
        self.draw_header()
        self.draw_grid()
        self.draw_side_panel()
        self.draw_footer()
        pygame.display.flip()


def main():
    game = PixelQuest()
    running = True

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    game.new_game()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                game.handle_click(event.pos)

        game.draw()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
