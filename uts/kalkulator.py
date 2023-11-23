angka_pertama = float(input("Masukkan angka pertama: "))
angka_kedua = float(input("Masukkan angka kedua: "))

print("|-----------------------|")
print("|Operator     Keterangan|")
print("|-----------------------|")
print("|   +           Tambah  |")
print("|-----------------------|")
print("|   -           Kurang  |")
print("|-----------------------|")
print("|   /            Bagi   |")
print("|-----------------------|")
print("|   *            Kali   |")
print("|-----------------------|")
print("|   **         Pangkat  |")
print("|-----------------------|")

operator = input("Pilih Operator (menggunakan simbol / karakter): ")

#Inisialisasi variabel hasil
hasil = 0

if operator == '+' or 'tambah' or 'Tambah':
    hasil = angka_pertama + angka_kedua
elif operator == '-' or 'kurang' or 'Kurang':
    hasil = angka_pertama - angka_kedua
elif operator == '*' or 'kali' or 'Kali':
    hasil = angka_pertama * angka_kedua
elif operator == '/' or 'bagi' or 'Bagi':
    hasil = angka_pertama / angka_kedua
elif operator == '**' or 'pangkat' or 'Pangkat':
    hasil = angka_pertama ** angka_kedua
else:
    print("Operator tidak valid")

print("Angka pertama:", angka_pertama)
print("Angka kedua:", angka_kedua)
print("Pilihan operator:", operator)
print("Hasil operator:", hasil)
