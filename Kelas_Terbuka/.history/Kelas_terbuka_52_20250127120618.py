import os
os.system("cls")
# Lambda function

def f_kuadrat(angka):
    return angka**2

print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

# kita pake lambda
# output = lambda argument: expression
kuadrat = lambda angka : angka**2
print(f"hasil lambda kuadrat = {kuadrat(5)}")

pangkat = lambda num,pow : num**pow
print(f"hasil lambda pangkat = {pangkat(4,2)}")

## kegunaan nya
# sorting untuk list biasa
data_list = ["otong", "ucup", "dudung"]
data_list.sort() # menjadi urutan alfabet
print(f"sorted list = {data_list}")

# sorting len pake panjang

def panjang_nama(nama):
    return len(nama)
    
data_list.sort(key=panjang_nama)
print(f"sorted list by panjang = {data_list}")

# sort pakai lambda
data_list = ["otong", "ucup", "dudung"]
data_list.sort(key = lambda nama : len(nama)) # "key =" itu adalah untuk mengurutkan element dalam daftar  % len(nama) untuk mengurutkan daftar berdasarkan panjang setiap nama

print(f"sorted list by lambda = {data_list}") 
#Ini adalah fungsi kecil yang disebut fungsi lambda. Fungsi lambda adalah cara untuk membuat fungsi sederhana tanpa harus memberi nama padanya.

# filter
'''filter (fungsi,iterable)'''
data_angka = [1,2,3,4,5,6,7]

def kurang_dari_lima(angka):
    return angka < 5
print(data_angka)

data_angka_baru = list(filter(kurang_dari_lima,data_angka))
                            #diawali fungsi, iterabel"adalah asal muasal
print(data_angka_baru)

data_angka_baru = list(filter(lambda x:x<7,data_angka))
                        #Fungsi filter() dalam Python menyaring elemen dari iterable (seperti list, tuple, atau set) berdasarkan kriteria yang ditentukan oleh sebuah fungsi.
                         #lambda x:x<7 adalah si x nya jadi parameter
print(data_angka_baru)

data_angka = [1,2,3,4,5,6,7]
# kasus genap
data_genap = list(filter(lambda x:(x%2==0),data_angka))
print(data_genap)

# kasus ganil
data_ganjil = list(filter(lambda x:(x%2!=0),data_angka))
print(data_ganjil)

# kelipatan 3
data_3 = list(filter(lambda x:(x%3==0),data_angka))
print(data_3)

# anonymous function
def pangkat (angka,n):
    hasil = angka**n
    return hasil

data_hasil = pangkat(5,2)
print(f"fungsi biasa = {data_hasil}")

# dengan currying menjadi

def pangkat(n):
    return lambda angka : angka**n

pangkat2 = pangkat(2)
print(f"pangkat 2 = {pangkat2(5)}")

pangkat3 = pangkat(3)
print(f"pangkat 3 = {pangkat3(3)}")
print(f"pangkat bebas = {pangkat(4)(5)}")

