buah_awal= ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
def duplikasi(daftar_buah):
    hasil_duplikasi = []

    #perulangan
    for buah in daftar_buah:
        hasil_duplikasi.append(buah)
        hasil_duplikasi.append(buah)

    return hasil_duplikasi

#proses
hasil = duplikasi(buah_awal)
print(hasil)