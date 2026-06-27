 
'''Latihan Fungsi'''
import os
os.system("cls")

# program hitung luas dan keliling

# # membuat header program
# os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# # Mengambil input user
# LEBAR = int(input('Masukan nilai lebar: '))
# PANJANG = int(input('Masukan nilai panjang:'))

# # Program menghitung luas
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR) 

# # tampilkan hasilnya

# '''Latihan Fungsi'''
# import os

# # program hitung luas dan keliling

# # membuat header program
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# # Mengambil input user
# LEBAR = int(input('Masukan nilai lebar: '))
# PANJANG = int(input('Masukan nilai panjang:'))

# # Program menghitung luas
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR) 

# # tampilkan hasilnya

# print(f"hasil perhitungan luas = {LUAS}")
# print(f"hasil perhitungan keliling = {KELILING}")

###Latihan = buat si user nya itu mau keliling saja atau luas saja

def header():
    '''fungsi header'''
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    '''fungsi input user'''
    # Mengambil input user
    lebar = int(input('Masukan nilai lebar: '))
    panjang = int(input('Masukan nilai panjang:'))
    
    return lebar,panjang
    
def hitung_luas(lebar,panjang):
    '''fungsi luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''fungsi keliling'''
    return 2*(lebar+panjang)
    
def display(message,value):
    '''fungsi display'''
    print(f"hasil perhitungan {message} = {value}")

# Program utamanya
while True:
    header()
    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)
    
    display("luas", LUAS)
    display("keliling",KELILING)
    
    isContinue = input("apakah lanjut (y/n)? ")
    if isContinue == "n":
        break
print("program selesai, terima kasih")
    
