hasil_akhir = [
{'nama':'Reza', 'nilai':70}, 
{'nama':'Ciut', 'nilai':63}, 
{'nama':'Dian', 'nilai':80}, 
{'nama':'Badu', 'nilai':40} 
]
def Lulus_saja(data):
    lulus = []
    for mhs in data:
        if mhs ['nilai'] > 65:
            lulus.append(mhs ['nama'])
    return lulus

print(Lulus_saja(hasil_akhir))