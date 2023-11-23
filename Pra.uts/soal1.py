# Input
nama_kendaraan = input("Nama kendaraan: ")
jenis_bensin = input("Jenis bensin: ")
kota_tujuan = input("Kota Tujuan: ")

# harga bensin
harga_pertalite = 10000
harga_pertamax = 14000
harga_premium = 17000

jarak_pertalite = 12
jarak_pertamax = 13
jarak_premium = 13.5

# validasi harga bensin dan jarak tempuh bensin
if jenis_bensin == "Pertalite":
    harga_per_liter = harga_pertalite
    jarak_per_liter = jarak_pertalite
elif jenis_bensin == "Pertamax":
    harga_per_liter = harga_pertamax
    jarak_per_liter = jarak_pertamax
else:
    harga_per_liter = harga_premium
    jarak_per_liter = jarak_premium

# jarak kota
if kota_tujuan == "Jakarta":
    jarak_kota = 20
elif kota_tujuan == "Bekasi":
    jarak_kota = 35.7
elif kota_tujuan == "Depok":
    jarak_kota = 5
elif kota_tujuan == "Tangerang":
    jarak_kota = 99
else:
    jarak_kota = 120.6

# kalkulasi output
pemakaian_bensin = jarak_kota / jarak_per_liter
total_harga = pemakaian_bensin * harga_per_liter

# Output
print("Nama kendaraan:", nama_kendaraan)
print("Jenis bensin:", jenis_bensin)
print("Kota Tujuan:", kota_tujuan)
print("Pemakaian bensin:", round(pemakaian_bensin, 2), "L")
print("Total harga dari bensin:", round(total_harga, 2), "IDR")