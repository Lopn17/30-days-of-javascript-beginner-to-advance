Gas, brooo 🔥 Day 2. Kita naik satu level.

Hari ini, tantangannya bukan sekadar mengubah tampilan website, tetapi membuat aplikasi yang harus **mengelola data dan menjaga konsistensi UI ketika pengguna berinteraksi dengannya.**

# 🗓️ Day 2 — Pixel Quest: Interactive Grid Game

**Difficulty:** Easy–Medium  
**Estimated time:** 45–90 menit  
**Tech stack:** HTML, CSS, Vanilla JavaScript

## 🎮 1. Project Concept

Bikin sebuah mini-game berbasis grid di mana pemain harus menemukan target tersembunyi di antara sejumlah kotak.

Setiap kotak bisa berinteraksi dengan pemain. Ada target yang harus ditemukan, jumlah percobaan yang terbatas, dan skor yang berubah berdasarkan hasil permainan.

Lo bebas menentukan tema visualnya: treasure hunt, sci-fi, dungeon, atau apa pun yang lo suka.

Yang penting, game-nya benar-benar berfungsi.

## 🎯 2. Objective

Bangun game berbasis grid yang memungkinkan pemain mencari target tersembunyi, mendapatkan skor, dan menyelesaikan permainan berdasarkan kondisi menang atau kalah.

## ⚙️ 3. Core Requirements

### A. Interactive Grid
- Tampilkan grid yang terdiri dari beberapa kotak interaktif.
- Pemain bisa memilih kotak dengan mengekliknya.
- Setiap kotak yang dipilih memberikan respons visual.
- Kotak yang sudah dipilih tidak bisa memberikan hasil baru ketika diklik berulang kali.

### B. Hidden Target
- Tempatkan target secara acak di dalam grid ketika permainan dimulai.
- Pemain harus menemukan target dengan memilih kotak.
- Posisi target harus ditentukan sebelum pemain mulai bermain.
- Target tidak boleh berpindah hanya karena pemain memilih kotak yang salah.

### C. Score & Attempts
- Tampilkan jumlah percobaan yang tersisa.
- Tampilkan skor pemain.
- Setiap pilihan kotak yang valid mengurangi jumlah percobaan.
- Menemukan target memberikan hasil yang berbeda dibandingkan memilih kotak yang salah.

### D. Win & Lose Conditions
- Pemain menang ketika berhasil menemukan target.
- Pemain kalah ketika seluruh percobaan habis tanpa menemukan target.
- Tampilkan pesan yang sesuai dengan hasil permainan.
- Setelah permainan berakhir, pemain tidak boleh melanjutkan permainan dengan memilih kotak lain.

### E. Restart Game
- Sediakan tombol untuk memulai permainan baru.
- Permainan baru harus memiliki target dan kondisi permainan yang baru.
- Skor, percobaan, dan kondisi interaksi harus sesuai dengan permainan baru.

## ✅ 3. Acceptance Criteria

Game lo dianggap berhasil jika:

- [ ] Grid ditampilkan dengan benar.
- [ ] Setiap kotak bisa dipilih.
- [ ] Target ditempatkan secara acak saat permainan dimulai.
- [ ] Target tidak berpindah selama satu permainan berlangsung.
- [ ] Kotak yang sudah dipilih tidak mengurangi percobaan lagi.
- [ ] Skor dan percobaan selalu sesuai dengan kondisi permainan.
- [ ] Pemain bisa menang dan kalah.
- [ ] Tidak ada interaksi permainan yang diterima setelah game berakhir.
- [ ] Restart menghasilkan permainan baru yang berfungsi dengan benar.
- [ ] Tidak ada masalah ketika pemain mengeklik kotak dengan cepat atau berulang kali.

## 🚧 4. Constraints

1. Gunakan HTML, CSS, dan Vanilla JavaScript.
2. Jangan menggunakan game engine atau library eksternal.
3. Jangan menggunakan backend atau database.
4. Grid harus dibuat secara dinamis atau terstruktur sehingga jumlah kotaknya tidak perlu ditulis satu per satu secara manual di HTML.
5. Logika permainan harus tetap berfungsi meskipun pemain melakukan interaksi dalam urutan yang tidak terduga.

Lo bebas menentukan ukuran grid, jumlah percobaan, sistem skor, dan desain visualnya, selama semua persyaratan utama terpenuhi.

## 🚀 5. Optional Stretch Goals

Kalau fitur utama sudah selesai, lo bisa memilih tantangan tambahan:

- **Difficulty Levels:** Sediakan mode Easy, Normal, dan Hard dengan tingkat kesulitan berbeda.
- **Best Score:** Simpan skor terbaik agar tetap tersedia setelah halaman di-refresh.
- **Timer:** Tambahkan batas waktu untuk menyelesaikan permainan.
- **Hints:** Berikan petunjuk terbatas yang membantu pemain menemukan target.
- **Statistics:** Catat jumlah kemenangan, kekalahan, dan rata-rata percobaan yang diperlukan untuk menemukan target.

Nggak perlu mengerjakan semuanya. Pilih stretch goal yang paling menarik buat lo.

---

## 🧠 Developer Mindset

Day 1 menguji kemampuan lo membuat UI yang bereaksi terhadap input.

**Day 2 menguji apakah lo bisa menjaga aturan permainan tetap konsisten meskipun banyak interaksi terjadi.**

Bayangkan beberapa situasi:
- Pemain mengeklik kotak yang sama berkali-kali.
- Pemain menemukan target pada percobaan terakhir.
- Pemain menekan restart setelah kalah.
- Pemain mencoba memilih kotak setelah menang.

Game lo harus menangani semua situasi tersebut dengan benar.

Gue nggak akan memberi tahu cara menyusun logika atau struktur kode untuk menyelesaikannya. Itu bagian dari tantangannya.

**Your mission: Build Pixel Quest.** 🎮

Kalau sudah selesai, kirim kode lo. Kita review hasilnya sebelum melanjutkan ke Day 3.