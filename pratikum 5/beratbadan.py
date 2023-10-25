print('''''
==============
Sistem penghitung berat badan Ideal
pilih jenis kelamin
1 = laki-laki
2 = Perempuan
''')

jk=int(input("Masukkan pilihan jenis kelamin"))
tinggi=int(input("Masukkan tinggi badan"))
match jk:
    case 1:
        ideal = (tinggi - 100)-(tinggi -100) *0,1 
        print("Berat badan ideal laki-laki untuk tinggi",tinggi, "adalah",ideal)
    case 2:
       ideal = (tinggi - 100) -(tinggi-100) *0,15
       print("Berat badan ideal perempuan untuk tinggi",tinggi, "adalah",ideal)
    case _:
         print("Pilihan yang anda masukkan tidak valid")