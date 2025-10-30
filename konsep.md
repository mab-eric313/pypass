# Tugas 1 RPL
1. Ide Awal Proyek
    - PyPass - Python Password Manager

2. End-user (pengguna)
    - Semua pengguna yang membutuhkan penyimpanan kata sandi yang aman

3. SDLC yang digunakan dan alasannya
    - **(Minggu ke-1 dan 2, 20-Okt - 01-Nov)** Setup kebutuhan project, seperti install python, python env, library yang digunakan, dll.

4. Rencana timeline pengerjaan sistem (20 Oktober 2025 - Januari)
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
