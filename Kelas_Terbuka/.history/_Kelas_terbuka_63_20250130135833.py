import os
os.systrm("cls")
# __main__ adalah top level code environment

# __name__ == *__main__" -> akan terjadi jika ada di file program utama
## __name__ pada file program utama
print(f"nilai __name__ pada main.py = '{__name__}'") # si name ini akan menjadi __main__ saat kita panggil sebagai program utama

## __name__ pada file program eksternal
import fungsi

## contoh penggunaan __main__

# deklarasi
def fungsi_tambah(a:int,b:int)-> int:
    return a + b

# fungsi utama
if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(angka1,angka2)
    print(f"hasil tambah = {hasil}")