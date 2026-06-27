import os
os.system("cls")
import Kelas_terbuka_57 # dia gak punya apa apa, karna berupa folder

hasil_tambah = Kelas_terbuka_57.matematik.tambah(1,2,3,4,45)
print(f"hasil tambah = {hasil_tambah}")

hasil_fisika = Kelas_terbuka_57.fisika.gaya(10,9.8)
print(f"hasil fisika = {hasil_fisika}")

hasil_kali = Kelas_terbuka_57.matematika.kali(1,3,4,5,6)
print(f"hasil kali = {hasil_kali}")

pangkat_3 = Kelas_terbuka_57.matematika.pangkat(3)
print(f"hasil pangkat 3 = {pangkat_3(5)}")

# from Kelas_terbuka_57 import * #->dia akan mencari __all__ di __init__.py

# hasil_tambah = matematika.basic.tambah(1,2,3,4,45)
# print(f"hasil tambah = {hasil_tambah}")

# hasil_fisika = fisika.gaya(10,9.8)
# print(f"hasil fisika = {hasil_fisika}")

# hasil_kali = matematika.basic.kali(1,3,4,5,6)
# print(f"hasil kali = {hasil_kali}")

