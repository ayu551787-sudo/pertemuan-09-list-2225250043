
print("A. Menelusuri List")
nilai = [75, 80, 65, 90, 88]
for x in nilai:
    print(x)

print("B. Menelusuri dengan Indeks")
nilai = [75, 80, 65, 90, 88]
for i in range(len(nilai)):
    print(f"Indeks {i}: {nilai[i]}")

print("C. Agregasi Dasar")
nilai = [75, 80, 65, 90, 88]
total = sum(nilai)
banyak = len(nilai)
rata_rata = total / banyak
tertinggi = max(nilai)
terendah = min(nilai)

print(f"Total = {total}")
print(f"Rata-rata = {rata_rata:.2f}")
print(f"Tertinggi = {tertinggi}")
print(f"Terendah = {terendah}")