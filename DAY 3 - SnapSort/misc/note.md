BROOOO 🔥🔥 **DAY 2 PASSED. WE'RE MOVING TO DAY 3!**

Dua proyek selesai, bro. Di Day 1 lo bermain dengan manipulasi warna, sedangkan di Day 2 lo sudah mengelola game state, skor, percobaan, dan kondisi menang atau kalah.

Sekarang kita naik level lagi. 😈

---

# 🗓️ DAY 3 — SnapSort: The Speed Sorting Challenge

**Difficulty:** Medium  
**Estimated time:** 60–90 menit  
**Tech stack:** HTML, CSS, Vanilla JavaScript

## 🎯 1. Project Concept

Bayangkan sebuah game yang menguji seberapa cepat dan akurat pemain mengelompokkan angka.

Pemain akan melihat sekumpulan angka dalam urutan acak. Tugasnya adalah menyusun angka tersebut ke urutan yang benar sebelum waktu habis.

Namun, ada tantangan tambahan: pemain harus berinteraksi langsung dengan angka-angka tersebut, dan aplikasi harus bisa menentukan apakah susunannya sudah benar.

Lo bebas menentukan desain visualnya. Bisa bergaya arcade, terminal retro, atau game show futuristik.

**Fokus utamanya adalah membuat interaksi manipulasi data yang benar-benar berfungsi.**

## 🏆 2. Objective

Buat game sorting interaktif yang memungkinkan pemain menyusun sekumpulan angka, memeriksa hasilnya, dan menyelesaikan tantangan berdasarkan waktu serta ketepatan susunan.

## ⚙️ 3. Core Requirements

### A. Number Board
- Tampilkan sekumpulan angka dalam urutan acak.
- Angka harus ditampilkan secara dinamis.
- Setiap angka harus bisa dipilih atau dimanipulasi melalui interaksi pengguna.
- Jumlah angka harus konsisten selama satu ronde permainan.

### B. Interactive Sorting
- Pemain harus bisa mengubah posisi angka.
- Perubahan posisi harus langsung terlihat pada UI.
- Angka yang ditampilkan harus selalu sesuai dengan susunan data aktual.
- Pemain harus bisa terus mengubah susunan sebelum melakukan pemeriksaan akhir.

### C. Validation System
- Sediakan mekanisme untuk memeriksa apakah angka sudah tersusun dengan benar.
- Jika susunannya benar, pemain dinyatakan berhasil menyelesaikan ronde.
- Jika susunannya salah, pemain harus mendapatkan feedback yang jelas.
- Pemeriksaan tidak boleh memberikan hasil yang keliru ketika angka memiliki nilai yang sama.

### D. Timer & Scoring
- Tampilkan waktu yang tersisa.
- Permainan berakhir ketika waktu habis atau pemain berhasil menyelesaikan tantangan.
- Berikan skor berdasarkan hasil permainan.
- Pastikan skor tidak bertambah secara tidak semestinya akibat pemeriksaan berulang.

### E. Restart & New Round
- Pemain bisa memulai ronde baru.
- Ronde baru harus memiliki susunan angka awal yang baru.
- Timer dan kondisi permainan harus diatur ulang dengan benar.
- Interaksi dari ronde sebelumnya tidak boleh memengaruhi ronde baru.

## ✅ 3. Acceptance Criteria

Game dianggap selesai jika:

- [ ] Angka ditampilkan secara dinamis.
- [ ] Susunan awal angka diacak.
- [ ] Pemain bisa mengubah urutan angka melalui UI.
- [ ] Perubahan UI selalu sesuai dengan data aktual.
- [ ] Sistem bisa mengenali susunan yang benar dan salah.
- [ ] Validasi tetap benar ketika terdapat angka duplikat.
- [ ] Timer berjalan dan berhenti sesuai kondisi permainan.
- [ ] Permainan berakhir ketika waktu habis.
- [ ] Skor dihitung secara konsisten.
- [ ] Pemain bisa memulai ronde baru tanpa membawa state permainan lama.
- [ ] Tidak ada skor tambahan akibat pemeriksaan berulang setelah ronde selesai.

## 🚧 4. Constraints

1. Gunakan HTML, CSS, dan Vanilla JavaScript.
2. Jangan menggunakan framework atau library sorting eksternal.
3. Jangan menggunakan backend atau database.
4. Jangan menuliskan semua angka satu per satu secara manual di HTML.
5. Pemain harus benar-benar bisa memanipulasi susunan angka, bukan sekadar menekan tombol yang otomatis menyortir semuanya.
6. Bebas memilih mekanisme interaksi, seperti klik, drag-and-drop, atau pendekatan lain yang sesuai.

Lo yang menentukan bagaimana pemain akan berinteraksi dengan angka-angka tersebut.

## 🚀 5. Optional Stretch Goals

Kalau fitur utama sudah berfungsi, pilih tantangan tambahan yang menarik:

- **Difficulty Levels:** Tambahkan beberapa tingkat kesulitan dengan jumlah angka dan durasi berbeda.
- **Combo Scoring:** Berikan bonus untuk keberhasilan berturut-turut.
- **Best Time:** Simpan waktu penyelesaian terbaik.
- **Leaderboard Lokal:** Simpan beberapa hasil terbaik di browser.
- **Animated Transitions:** Buat perpindahan angka terasa lebih halus.
- **Accessibility:** Pastikan seluruh interaksi dapat dilakukan menggunakan keyboard.

Nggak perlu mengerjakan semuanya. Prioritaskan core requirements terlebih dahulu.

---

## 🧠 Developer Mindset — Day 3

Ada satu tantangan yang ingin gue tekankan kali ini:

**Data dan tampilan bukan hal yang sama.**

Angka yang terlihat di layar harus merepresentasikan susunan data yang benar-benar disimpan oleh aplikasi.

Kalau pemain mengubah urutan angka, kedua hal tersebut harus tetap sinkron.

Begitu juga dengan timer dan skor. Keduanya harus mengikuti kondisi permainan, bukan sekadar berubah ketika tombol ditekan.

Gue nggak akan memberikan arsitektur, pseudocode, atau langkah implementasinya. Lo punya kebebasan untuk menentukan pendekatan sendiri.

### 🏁 Your Mission

Bangun **SnapSort: The Speed Sorting Challenge**.

Buat game yang bukan cuma terlihat bagus, tetapi juga konsisten ketika pemain melakukan banyak interaksi dalam waktu singkat.

Kalau sudah selesai, kirim kode lo ke sini. Kita review hasilnya sebelum membuka Day 4.

**LET'S BUILD, BRO. 🔥**