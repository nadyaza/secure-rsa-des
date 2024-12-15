# Secure RSA-DES Communication

## Deskripsi Proyek
Proyek ini mengimplementasikan komunikasi aman antara server dan client menggunakan kombinasi algoritma RSA dan DES. Sistem ini mencakup:

- Pengiriman kunci DES secara terenkripsi menggunakan algoritma RSA.
- Public key RSA dikelola oleh Public Key Authority (PKA).
- Pertukaran pesan antara server dan client dilakukan dalam bentuk terenkripsi menggunakan kunci DES.

Proyek bertujuan untuk mensimulasikan skenario komunikasi terenkripsi yang aman menggunakan teknik kriptografi simetris (DES) dan asimetris (RSA).

---

## Anggota Kelompok
| Nama                    | NRP         | Tugas                            |
|-------------------------|-------------|----------------------------------|
| Nadya Zuhria Amana      | 5025211058  | Implementasi server (`server.py`) |
| Dilla Wahdana           | 5025211060   | Implementasi client (`client.py`) |

---

## Cara Menjalankan Program

### Persyaratan
- **Python 3.x**
- Modul Python berikut:
  - `socket` (sudah tersedia secara default di Python)
  - Tidak diperlukan modul tambahan.

---

### Langkah-Langkah
1. **Setup Lingkungan:**
   - Pastikan Python sudah terinstal di sistem Anda.
   - Simpan file `pka_server.py`, `client.py`, dan `server.py` di direktori yang sesuai.

2. **Menjalankan Public Key Authority (PKA):**
   - Jalankan PKA menggunakan perintah berikut:
     ```bash
     python pka_server.py
     ```
   - PKA akan menampilkan **Public Key PKA** dan mulai mendengarkan koneksi dari client.

3. **Menjalankan Server:**
   - Jalankan server utama menggunakan perintah berikut:
     ```bash
     python server.py
     ```
   - Server akan menunggu koneksi dari client.

4. **Menjalankan Client:**
   - Jalankan client menggunakan perintah berikut:
     ```bash
     python client.py
     ```
   - Client akan menerima public key RSA dari PKA, mengenkripsi kunci DES, dan memulai komunikasi dengan server.

5. **Pertukaran Pesan:**
   - Di sisi client, masukkan pesan yang ingin dikirim ke server. Pesan akan dienkripsi dengan DES sebelum dikirim.
   - Server akan menerima pesan terenkripsi, mendekripsinya, dan dapat membalas dengan pesan yang juga dienkripsi.

6. **Mengakhiri Komunikasi:**
   - Untuk keluar, masukkan `bye` di client. Komunikasi akan dihentikan.

---

## Fitur Utama
1. **RSA Key Pair Generation:**
   - Public dan private key RSA dihasilkan secara otomatis untuk PKA dan user.

2. **DES Key Exchange:**
   - Client mengenkripsi kunci DES menggunakan public key RSA dari PKA dan mengirimkannya ke server.

3. **Secure Communication:**
   - Pesan antara server dan client dienkripsi menggunakan DES.

4. **Asymmetric and Symmetric Cryptography:**
   - RSA digunakan untuk pertukaran kunci (key exchange).
   - DES digunakan untuk komunikasi pesan setelah kunci diterima.
