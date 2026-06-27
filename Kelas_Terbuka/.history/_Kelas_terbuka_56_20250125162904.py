import os
os.system("cls")

import Kelas_terbuka_56.matematika 
from Kelas_terbuka_56 import fisika
from Kelas_terbuka_56.fisika import gaya as force


# Kelas_terbuka_56 -> nama package sub sesuai folder
# matematika -> nama modul

hasil_tambah = Kelas_terbuka_56.matematika.tambah(1,2,3,4,5)
print(f"hasil tambah dari package adalah = {hasil_tambah}")

gaya = fisika.gaya(90,10)
print(f"gaya adalah = {gaya}")


gaya = force(90,10)
print(f"gaya adalah = {gaya}")