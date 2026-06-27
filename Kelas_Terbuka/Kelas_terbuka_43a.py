# tamplate dict mahasiswa 
import datetime as dt
import os

mahasiswa_template = {
   'nama': 'nama',
   'nim': '00000000', 
   'sks_lulus': 0,
   'lahir': dt.datetime(1111,1,11)
}

data_mahasiswa = {}

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

print(mahasiswa)