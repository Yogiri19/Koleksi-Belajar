import os
os.system("cls")
# __main__ -> adalah top leve code environment

# __name__ == "__name__" -> akan terjadi 
# jika ada di program utama

# __name__ pada file program utama
print(f"nilai __name__ pada main.py = '{__name__}'")

## __name__ pada file program eksternal
import fungsi

## contoh penggunaan __main__

# deklarasi
def fungsi_tambah(a:int,b:int)-> int:
    return a+b
# fungsi utamanya