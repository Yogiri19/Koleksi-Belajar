import os
os.system("cls")
# import

# fungsinya adalah untuk mengambil 
# program dari file external .py

# 1. untuk menyambung program dari external
import abc_1
# 2. import dengan data
import bayo

# data ada di namespace variable
print(bayo.data)

# 3. import dengan fungsi
import fungsi

hasil = fungsi.tambah(4,5)
print(hasil) 