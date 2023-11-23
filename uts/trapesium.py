# PSEDUCODE PENGHITUNGAN LUAS DAN KELILING TRAPESIUM
# 1. Masukkan panjang sisi atas trapesium (a)
# 2. Masukkan panjang sisi bawah trapesium (b)
# 3. Masukkan tinggi trapesium (h)
# 4. Hitung luas trapesium: luas = 0.5 * (a + b) * h
# 5. Hitung keliling trapesium: keliling = a + b + (2 * sisi miring)
# 6. Tampilkan luas dan keliling trapezium

# PROGRAM PYTHON PENGHITUNGAN LUAS DAN KELILING TRAPESIUM
a = float(input("Masukkan panjang sisi atas trapesium: "))
b = float(input("Masukkan panjang sisi bawah trapesium: "))
h = float(input("Masukkan tinggi trapesium: "))

luas = 0.5 * (a + b) * h

keliling = a + b + (2 * ((a - b) ** 2 + h ** 2) ** 0.5)
hasil_akhir_keliling = round(keliling, 2)

#Menampilkan luas dan keliling trapesium
print("Luas trapesium:", luas)
print("Keliling trapesium:", hasil_akhir_keliling)