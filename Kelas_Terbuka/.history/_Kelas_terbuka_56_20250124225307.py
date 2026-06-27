import os
os.system("cls")

import Kelas_terbuka_56.matematika 

from . import fisika


# Kelas_terbuka_56 -> nama package sesuai folder
# matematika -> nama modul

hasil_tambah = Kelas_terbuka_56.matematika.tambah(1,2,3,4,5)
print(f"hasil tambah dari package adalah = {hasil_tambah}")

gaya = fisika.gaya(90,10)
print(f"gaya adalah = {gaya}")