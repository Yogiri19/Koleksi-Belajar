import os
os.system("cls")
# Module matematika dengan import

from matematika import tambah, kali, pangkat # bisa memakai "," untuk mengambil lebih dari 2
from matematika import * # "*"ini semua mengambil dari matematika

hasil_tambah = tambah(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = kali(1,2,3,4,5)
print(f"hasil kali = {hasil_kali}")

pangkat_3 = pangkat(3)
print(f"pangkat 3 = {pangkat_3(3)}")
