import os
os.system("cls")
''' Fungsi dengan argument (input)'''

# Template
# def nama_fungsi(argument):
#     Badan fungsi
   
   
def hello_world(nama):
   '''fungsi hello world menerima input dengan variable nama'''
   print(f"Selamat datang dunia wahai {nama}")

hello_world("ucup")   
hello_world("asep")   
      
# program tambah

def tambah(angka_1,angka_2):
   '''fungsi tambah'''
   hasil = angka_1 + angka_2
   print(f"{angka_1} + {angka_2} = {hasil}")
   
tambah(1,5)
tambah(100000,1)
   
def say_hi(list_peserta):
   '''fungsi say hi'''
   data_peserta = list_peserta
   for peserta in data_peserta:
      print(f"yang terhomat {peserta}")
      
nama = ["ucup","otong","dudung"]

say_hi(nama)