motor = {"beat", "vario", "supra "}
mobil = {"lamborgini", "ferrari", "avanza"}
print(motor)

#menambahkan item
motor.add("Nmax")
print(motor)

#menghapus ite,
motor.remove("vario")
print(motor)

#menggabungkan set
kendaraan = motor.union(mobil)
print(kendaraan)

#update
motor.update(mobil)
print(motor)