buah_awal = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
def balikantulisan(daftar_buah):
    hasil_balik = []

    #menghitung panjang dan jumlah dalam list
    panjang_daftar = len(daftar_buah)

    #perulangan
    for buah in range(panjang_daftar - 1, -1, -1):
        hasil_balik.append(daftar_buah[buah])

    return hasil_balik
#proses 
hasil = balikantulisan(buah_awal)
print(hasil)