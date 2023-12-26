class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

# Contoh penggunaan
animal1 = Animal("Singa", "Daging", "Darat", "Vivipar")
print(f"Nama: {animal1.name}")
print(f"Makanan: {animal1.makanan}")
print(f"Habitat: {animal1.hidup}")
print(f"Cara Berkembang Biak: {animal1.berkembang_biak}")