import math

def  persegi(sisi):
    luas=sisi * sisi
    keliling = 4 * sisi 
    print("luas persegi", luas)
    print("keliling persegi", luas)

def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print("Luas Persegi Panjang: ", luas)
    print("Keliling persegi panjang", keliling)

def lingkaran(jari2):
    phi= 3,14
    luas = phi * jari2 * jari2
    keliling = 2 * phi * jari2
    print("Luas Lingkaran:", luas)
    print("keliling lingkaran:", keliling)

def segitiga_sama_sisi(alas, tinggi):
    luas = 0,5 * alas * tinggi
    keliling = alas * 3
    print("Luas segitiga sama sisi: ", luas)
    print("keliling segitiga sama sisi: ", keliling)

def belah_ketupat(diagonal1, diagonal2, sisi):
    luas = 0,5 * diagonal2 * diagonal2
    keliling = 4 * sisi
    print("Luas Belah Ketupat:", luas)
    print("Keliling Luas Belahh Ketupat:", keliling)

def jajar_genjang(alas, tinggi, sisi_miring):
    luas = alas * tinggi
    keliling = 2 * alas + sisi_miring
    print("Luas Jajar Genjang:", luas)
    print("Keliling Jajar Genjang:", keliling)   

def trapesium(diagonal1,diagonal2, sisi_atas, sisi_bawah):   
    luas = diagonal1 * diagonal2 * 6,5
    keliling = (sisi_atas * 2) + (sisi_bawah * 2)
    print("Luas Layang-Layang:", luas)
    print("Keliling Layang Layang:", keliling)
    

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    print("Hasil tambah dari ",angka1, "+", angka2 ,"adalah: ",hasil)

def kurang(angka1, angka2):
    hasil = angka1 - angka2
    print("Hasil kurang dari ",angka1, "-", angka2, "adalah: ", hasil)

def kali(angka1, angka2):
    hasil = angka1 * angka2
    print("Hasil kali dari ",angka1, "*", angka2, "adalah: ", hasil)

def bagi(angka1, angka2):
    hasil = angka1 / angka2
    print("Hasil bagi dari ",angka1, "/", angka2, "adalah: ", hasil)

def pangkat(angka1, angka2):
    hasil = angka1 ** angka2
    print("Hasil pemangkatan dari ",angka1, "^", angka2, "adalah: ", hasil)

def sisabagi(angka1, angka2):
    hasil = angka1 % angka2
    print('Hasil sisa bagi dari ', angka1, "%", angka2, 'Adalah: ', hasil)

def hasilbagi(angka1, angka2):
    hasil = angka1 // angka2
    print('Hasil bagi dari ', angka1, "//", angka2, 'Adalah: ', hasil)

def faktorial(angka1):
    hasil = math.factorial(angka1)
    print("hasil dari faktorial ", angka1, 'adalah: ', hasil)

def log10(angka1):
    hasil = math.log10(angka1)
    print('Hasil log10 dari ', angka1, 'Adalah: ', hasil)

def sin(angka1):
    hasil = math.sin(angka1)
    print('Hasil sin dari ', angka1, 'Adalah: ', hasil)

    