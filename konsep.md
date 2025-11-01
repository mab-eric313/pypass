# Tugas 1 RPL
1. Ide Awal Proyek
    - PyPass - Python Password Manager

2. End-user (pengguna)
    - Semua pengguna yang membutuhkan penyimpanan kata sandi yang aman

3. SDLC yang digunakan dan alasannya
    - SDLC: Agile
        - Alur siklus pengembangan:
            1. Planning & Analysis
            2. design
            3. coding
            4. testing
            5. deployment
            6. maintenance
        - Alasan:
            1. Adaptif terhadap perubahan
            2. Cepat menghasilkan fungsional di setiap siklus
            3. Stabilitas aplikasi terjaga

4. Rencana timeline pengerjaan sistem (20 Oktober 2025 - Januari)
    - **Akhir Oktober** Setup kebutuhan project, seperti install python, python env, library yang digunakan, dll.
    - **Pertengahan November** 
        - CLI: 
            1. `(crypto.py)` Membangun dan memastikan fondasi enkripsi dan dekripsi berjalan dengan baik
            2. `(database.py)` Membangun kerangka database `insert`, `get`, `list`, dan `delete` entri
        - GUI: `(gui.py)` Membangun kerangka tampilan awal
    - **Akhir November** Versi `0.1-devel`
        - CLI: 
            1. `(core.py)` Membuat class `PasswordManager` yang menggabungkan `crypto.py` dan `database.py`
            2. `(cli.py)` Menambahkan argparse untuk init vault, unlock, add, get, list, dan delete
        - GUI: Menambahkan `Tambah Kata Sandi` dan list aplikasi
        - Testing: `encrypt` -> `store` -> `retrieve` -> `decrypt`
    - **Pertengahan Desember** 
        - CLI: Menambahkan opsi `--gen-pass` untuk men-generate password
        - GUI: Menambahkan tombol `Add`, `Edit`, `Delete` dan kotak teks akun dan kata sandi
    - **Akhir Desember** Versi `0.2-devel`
        - CLI: Tambahkan backup/restore
        - GUI: 
            1. Di `Add password` tambahkan `Site`, `Username`, `Password`, `Note`
            2. Buat halaman aplikasi dan `Tambahkan kata sandi` berfungsi
    - **Pertengahan Januari**
        - GUI: 
            1. Tambahkan clipboard handling - auto-clear setelah beberapa waktu
            2. Tambahkan tombol backup/restore 
    - **Akhir Januari** Versi `1.0-beta`
        - Jaga stabilitas, perbaiki bug dan error jika ada
        - GUI: Poles UI

5. Kebutuhan awal sistem (fitur) yang akan dikembangkan, arsitektur sistem (web based, mobile based, desktop based)
    - Fitur (Kebutuhan Fungsional):
        1. Sebagai tempat menyimpan kata sandi
        2. Dapat membuat kata sandi yang kuat
        3. Memanajemen data kredensial
        4. Keamanan data yang terjamin
        5. Dapat mencadangkan atau memulihkan database yang sudah terenkripsi

6. Lingkungan pengembangan sistem dan rencana pengembangan sistem (OS, bahasa pemrograman, framework dan tools yang digunakan).
    - Lingkungan pengembangan:
        - OS: Windows dan Linux
        - Version Control System: Git/Github
        - Lingkungan isolasi: Python Virtual Environment
    - Rencana Pengembangan:
        - Bahasa pemrograman: Python
        - Framework/Library:
            1. Qt (PySide6) -> GUI
            2. cryptography -> enkripsi password
            3. secrets      -> generator password
            4. sqlite3      -> database lokal
            5. pyperclip    -> menyalin password sementara ke clipboard
            6. pytest       -> uji keamanan fungsi enkripsi/dekripsi
