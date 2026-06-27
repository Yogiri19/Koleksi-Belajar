# tamplate dict mahasiswa 
import datetime as dt
import os
import string
import random
mahasiswa_template = {
   'nama': 'nama',
   'nim': '00000000', 
   'sks_lulus': 0,
   'lahir': dt.datetime(1111,1,11)
}

data_mahasiswa = {}
while True:
   os.system("cls") # untuk windows
   #os.system("clear") # untuk linux,mac

   print(f"{'SELAMAT DATANG':^20}")
   print(f"{'DATA MAHASISWA':^20}")
   print("-"*20)

   mahasiswa = dict.fromkeys(mahasiswa_template.keys())
   mahasiswa['nama'] = input("Nama Mahasiswa:")
   mahasiswa['nim'] = input("Nim Mahasiswa:")
   mahasiswa['sks_lulus'] = int(input("Sks Lulus: "))

   Tahun_lahir = int(input("Tahun lahir (YYYY): "))
   Bulan_lahir = int(input("Bulan lahir (1-12): "))
   Tanggal_lahir = int(input("Tanggal lahir (1-31): "))
   mahasiswa['lahir'] = dt.datetime(Tahun_lahir,Bulan_lahir,Tanggal_lahir)

   KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
   data_mahasiswa.update({KEY:mahasiswa})
   # dari tutorial sebelumnya, hilangkan beasiswa
   print(f"\n{'KEY':<6} {'NAMA':<17} {'NIM':<8} {'SKS Lulus':^18} {'Tanggal Lahir':<10}")  
   print('-'*60)

   for mahasiswa in data_mahasiswa:
      KEY = mahasiswa
      NAMA = data_mahasiswa[KEY] ['nama'] 
      NIM = data_mahasiswa[KEY] ['nim']
      SKS = data_mahasiswa[KEY] ['sks_lulus']  
      LAHIR = data_mahasiswa[KEY] ['lahir'].strftime("%x")
      
      print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^18} {LAHIR:<10}")  

   print("\n")
   is_done = input("Mau tambah lagi bro (y/n)? ")
   if is_done == "n":
      break
   
print("\nAkhir dari program, Terimakasih")

