print("\n--- D. Menghitung Kelulusan (Seleksi & Pencacahan) ---")
# Data nilai untuk pengecekan kelulusan (standar KKM misal >= 60)
nilai_ujian = [75, 80, 55, 90, 60, 48]
jumlah_lulus = 0

for x in nilai_ujian:
    if x >= 60:
        jumlah_lulus += 1

print(f"Daftar nilai ujian: {nilai_ujian}")
print(f"Jumlah lulus = {jumlah_lulus}")