
print("A. Fungsi Rata-Rata")

def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

# Pengujian dengan kumpulan data yang berbeda
nilai_a = [75, 80, 90]
nilai_b = [60, 70, 85, 95]

print("Rata-rata Nilai A:", rata_rata(nilai_a))
print("Rata-rata Nilai B:", rata_rata(nilai_b))


print("B. Fungsi Statistik Ringkas")

def statistik(data):
    return {
        "banyak": len(data),
        "total": sum(data),
        "minimum": min(data),
        "maksimum": max(data),
        "rata_rata": sum(data) / len(data)
    }

# Pengujian fungsi statistik ringkas
nilai = [75, 80, 65, 90, 88]
hasil = statistik(nilai)

print("Hasil Statistik Ringkas:")
print(hasil)