import Kelas_terbuka_56.matematika 
# Kelas_terbuka_56 -> nama package sesuai folder
# matematika -> nama modul

hasil_tambah = Kelas_terbuka_56.matematika.tambah(1,2,3,4,5)
print(f"hasil tambah dari package adalah = {hasil_tambah}")
''' Module matematika'''
def tambah(*args):
    hasil = 0
    for data in args:
        hasil += data

    return hasil

def kali(*args):
    hasil = 1
    for data in args:
        hasil *= data

    return hasil

def pangkat(n):
    return lambda angka:angka**n