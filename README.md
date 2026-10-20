# Pertemuan 09 - List dan Pengolahan Data Numerik

Nama: Ayu Syarifatu Zahra
NIM: 2225250043
Kelas: 3B

## Tujuan
Mengolah kumpulan data numerik dengan list Python.

## Struktur Program
- `latihan/`: Folder berisi script latihan dasar konsep list:
  - `01_buat_list.py`: Dasar pembuatan list dan tipe datanya.
  - `02_indeks_slicing.py`: Contoh akses elemen dan slicing list.
  - `03_manipulasi_list.py`: Contoh append, insert, remove, pop, sort, dan reverse.
  - `04_agregasi_nilai.py`: Contoh pencarian total, rata-rata, min, max.
  - `05_filter_kelulusan.py`: Contoh penyaringan data nilai lulus.
  - `06_fungsi_statistik.py`: Penerapan fungsi dengan parameter list.
- `praktik/`: Folder berisi program utama praktik:
  - `analisis_nilai_mahasiswa.py`: Program analisis nilai mahasiswa yang menghasilkan ringkasan statistik dan filter kelulusan.

## Cara Menjalankan
Jalankan perintah berikut di terminal:

```bash
python3 praktik/analisis_nilai_mahasiswa.py

## Test Case

| Data Input | Yang Diperiksa | Hasil Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- | :---: |
| `[60, 70, 80]` | Rata-rata | 70.00 | 70.00 | Pass |
| `[60, 70, 80]` | Minimum / Maksimum | 60 / 80 | 60 / 80 | Pass |
| `[60, 70, 80]` | Jumlah lulus | 3 | 3 | Pass |
| `[59, 60, 61]` | Batas kelulusan | 2 lulus | 2 lulus | Pass |
| `[]` | Penanganan list kosong pada fungsi `rata_rata` | Tidak error | Tidak error | Pass |

## Refleksi
1. Hal yang dipahami tentang indeks/list: Indeks dalam Python dimulai dari 0 dan kita bisa menggunakan indeks negatif untuk mengakses elemen dari arah belakang. Penggunaan list numerik sangat memudahkan perhitungan matematika seperti sum(), min(), max(), dan rata-rata.
2. Kesalahan yang berhasil diperbaiki: Mengatasi potensi error ZeroDivisionError pada fungsi rata_rata ketika list input berupa list kosong ([]) dengan menambahkan kondisi pemeriksaan if len(data) == 0: sebelum melakukan pembagian.
