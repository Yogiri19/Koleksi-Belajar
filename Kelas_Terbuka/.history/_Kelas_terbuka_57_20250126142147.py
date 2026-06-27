import os

os.system("cls")

# # import Kelas_terbuka_57 # dia gak punya apa apa, karna berupa folder
# from Kelas_terbuka_57 import *

# hasil_tambah = Kelas_terbuka_57.matematika.basic.tambah(1,2,3,4,45)
# print(f"hasil tambah = {hasil_tambah}")

# hasil_fisika = Kelas_terbuka_57.fisika.gaya(10,9.8)
# print(f"hasil fisika = {hasil_fisika}")

# hasil_kali = Kelas_terbuka_57.matematika.basic.kali(1,3,4,5,6)
# print(f"hasil kali = {hasil_kali}")

from Kelas_terbuka_57 import *

hasil_tambah = matematika.basic.tambah(1,2,3,4,45)
print(f"hasil tambah = {hasil_tambah}")

hasil_fisika = fisika.gaya(10,9.8)
print(f"hasil fisika = {hasil_fisika}")

hasil_kali = matematika.basic.kali(1,3,4,5,6)
print(f"hasil kali = {hasil_kali}")
