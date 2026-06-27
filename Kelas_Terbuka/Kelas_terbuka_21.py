 #If dan Else Statment
# 1. if nya
# 2. kondisinya
# 3. aksinya

nama = input("masukan nama anda:")

# program sebelumnya
# if kondisi: aksi
# program selanjutnya

# 1. program if inline
if nama =="fakhri" : print("kamu ganteng abis")
print("akhir dari program")
print(f"Terima kasih {nama} ")
print("========1=========")

# 2. program if indentation (dia mendorong ke dalam)
if nama == "dinal":
    print(f"kamu ganteng {nama}")
print(f"Terima kasih {nama} ")


# 3. Else Statment (kalo benar akan dijalankan menggunakan "if" tapi kalo salah akan dijalankan menggunakan "else")
nama = input("masukan nama anda:")

if nama == "bayo": 
    print("hai bayo, si keren ")
else:
    print("ah kamu bukan bayo, kamu gak keren")
    print(5*"-", "kamu gak keren", 5*"-") 