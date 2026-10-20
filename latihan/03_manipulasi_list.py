# Inisialisasi data awal sesuai contoh manipulasi
nilai = [75, 80, 65]

print("--- 4. Manipulasi Elemen List ---")
print("List awal:", nilai)

# Menambah elemen di akhir list
nilai.append(90)
print("Setelah append(90):", nilai)

# Mengubah elemen pada indeks tertentu
nilai[1] = 82
print("Setelah nilai[1] = 82:", nilai)

# Menyisipkan elemen pada indeks tertentu
nilai.insert(2, 70)
print("Setelah insert(2, 70):", nilai)

# Menghapus elemen berdasarkan nilai spesifik
nilai.remove(65)
print("Setelah remove(65):", nilai)

# Menghapus elemen berdasarkan indeks
dihapus = nilai.pop(0)
print(f"Setelah pop(0) (menghapus nilai {dihapus}):", nilai)

# Mengurutkan list secara menaik (ascending)
nilai.sort()
print("Setelah sort():", nilai)

# Membalik posisi elemen di dalam list
nilai.reverse()
print("Setelah reverse():", nilai)