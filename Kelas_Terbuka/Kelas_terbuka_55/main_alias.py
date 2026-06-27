import os
os.system("cls")
# Module matematika dengan import

#from matematika import tambah, kali, pangkat  # bisa memakai "," untuk mengambil lebih dari 2
from matematika import tambah as add # as itu adalah alias atau sebagai
from matematika import kali as fahri
from matematika import pangkat as bayo
#from matematika import * # "*"ini semua mengambil dari matematika

import matematika as math 

 
hasil_tambah = add(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = math.kali(1,2,3,4,5)
print(f"hasil kali = {hasil_kali}")

pangkat_3 = bayo(3)
print(f"pangkat 3 = {pangkat_3(3)}")
