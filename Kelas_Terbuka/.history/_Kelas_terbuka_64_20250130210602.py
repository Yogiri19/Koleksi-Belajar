import os
os.system("cls")
## tutorial membaca file eksternal

print(3 * "=", "Membaca file txt", 3 * "=")
file = open("data.txt",mode = "r")

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")

## baca seluruh file
#print(file.read())

## baca per baris
# print(file.readline()) # baca baris pertama
# print(file.readline()) # baca baris kedua

## baca semua baris sebagai list
print(file.readlines())