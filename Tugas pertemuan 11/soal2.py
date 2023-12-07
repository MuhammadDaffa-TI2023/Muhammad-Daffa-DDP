# Modul operasi_aritmatika.py

def tambahkan(angka1, angka2):
    return angka1 + angka2

def kurangkan(angka1, angka2):
    return angka1 - angka2

def kalikan(angka1, angka2):
    return angka1 * angka2

def bagi(angka1, angka2):
    if angka2 != 0:
        return angka1 / angka2
    else:
        return "Error: Pembagian oleh nol"

def bagi_bulat(angka1, angka2):
    if angka2 != 0:
        return angka1 // angka2
    else:
        return "Error: Pembagian oleh nol"

def modulus(angka1, angka2):
    if angka2 != 0:
        return angka1 % angka2
    else:
        return "Error: Pembagian oleh nol"

def pangkat(angka, eksponen):
    return angka ** eksponen