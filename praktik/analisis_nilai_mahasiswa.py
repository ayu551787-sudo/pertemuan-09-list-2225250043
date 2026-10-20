
def rata_rata(data):
    """Menghitung rata-rata dari list data dengan penanganan list kosong."""
    if len(data) == 0:
        return 0.0
    return sum(data) / len(data)

def nilai_lulus(data, batas=60):
    """Menyaring dan mengembalikan list baru yang berisi nilai mahasiswa yang lulus."""
    list_lulus = []
    for nilai_mhs in data:
        if nilai_mhs >= batas:
            list_lulus.append(nilai_mhs)
    return list_lulus

# 1. Simpan minimal 10 nilai dalam sebuah list
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

print("=" * 45)
print("     PROGRAM ANALISIS NILAI MAHASISWA")
print("=" * 45)

# 2. Tampilkan seluruh data dan banyak data
print(f"Seluruh Data Nilai  : {nilai}")
print(f"Banyak Data (Total) : {len(nilai)} mahasiswa")

# 3. Hitung total, rata-rata, nilai minimum, dan maksimum
total_nilai = sum(nilai)
rerata_nilai = rata_rata(nilai)
nilai_min = min(nilai)
nilai_max = max(nilai)

print("RINGKASAN STATISTIK")
print(f"Total Nilai         : {total_nilai}")
print(f"Rata-rata           : {rerata_nilai:.2f}")
print(f"Nilai Minimum       : {nilai_min}")
print(f"Nilai Maksimum      : {nilai_max}")

# 4, 5, & 6. Batas kelulusan, hitung jumlah lulus/belum, dan buat list baru
batas_kkm = 60
daftar_lulus = nilai_lulus(nilai, batas_kkm)
jumlah_lulus = len(daftar_lulus)
jumlah_belum_lulus = len(nilai) - jumlah_lulus

print("INFORMASI KELULUSAN (Batas: 60)")
print(f"Daftar Nilai Lulus  : {daftar_lulus}")
print(f"Jumlah Lulus        : {jumlah_lulus} mahasiswa")
print(f"Jumlah Belum Lulus  : {jumlah_belum_lulus} mahasiswa")
print("=" * 45)

print("\n" + "=" * 50)
print("     MENJALANKAN TEST CASE WAJIB")
print("=" * 50)

# Test Case 1: 
tc1_data = [60, 70, 80]
tc1_hasil = rata_rata(tc1_data)
print(f"Test Case 1 (Rata-rata): Data {tc1_data}")
print(f"-> Hasil Aktual: {tc1_hasil:.2f} | Harapan: 70.00")

# Test Case 2: 
tc2_data = [60, 70, 80]
print(f"\nTest Case 2 (Min/Max): Data {tc2_data}")
print(f"-> Hasil Aktual: Min={min(tc2_data)} / Max={max(tc2_data)} | Harapan: 60 / 80")

# Test Case 3: 
tc3_data = [60, 70, 80]
tc3_hasil = len(nilai_lulus(tc3_data, 60))
print(f"\nTest Case 3 (Jumlah Lulus): Data {tc3_data}")
print(f"-> Hasil Aktual: {tc3_hasil} lulus | Harapan: 3")

# Test Case 4: 
tc4_data = [59, 60, 61]
tc4_hasil = len(nilai_lulus(tc4_data, 60))
print(f"\nTest Case 4 (Batas Kelulusan 60): Data {tc4_data}")
print(f"-> Hasil Aktual: {tc4_hasil} lulus | Harapan: 2 lulus")

# Test Case 5: 
tc5_data = []
try:
    tc5_hasil = rata_rata(tc5_data)
    print(f"\nTest Case 5 (List Kosong): Data {tc5_data}")
    print(f"-> Hasil Aktual: {tc5_hasil} (Aman, Tidak Error) | Harapan: Tidak error")
except Exception as e:
    print(f"\nTest Case 5 (List Kosong): Gagal dengan error {e}")

print("=" * 50)