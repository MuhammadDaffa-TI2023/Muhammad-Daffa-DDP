data_diri = {"nama" :"Dafa", "mapel":"DDP"}

#mengakses dictionary
print(data_diri)

#menambah item
data_diri["jurusan"] = "Teknik Informatika"
print(data_diri)

#update item
data_diri["nama"] = "Muhammad Daffa"
print(data_diri)

#menghapus 
data_diri.pop("mapel")
print(data_diri)

#cek keberadaan key 
if "nama" in data_diri:
    print("terdapat nama")
else:
    print("Tidak ada nama")