luas_bangun_datar = int(input("menghitung luas bangun datar:"))
match luas_bangun_datar:
    case 1:
        panjang_sisi = int(input("masukkkan sisi persegi :"))
        hasil1= panjang_sisi + panjang_sisi
        print("luas persegi adalah :",hasil1)
    case 2:
        jari_jari = int(input("masukkan jari jari lingkaran"))
        hasil2=3.14 * jari_jari * jari_jari
        print("luas lingkaran adalah :",hasil2)
    case 3:
        alas= int(input("Masukkan alas"))
        tinggi=int(input("Masukkan tinggi"))
        hasil3=0,5* alas * tinggi
        print("luas segitiga adalah :",hasil3)