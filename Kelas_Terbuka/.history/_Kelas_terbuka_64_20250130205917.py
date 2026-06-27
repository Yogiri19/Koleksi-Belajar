import os
os.system("cls")
## tutorial membaca file eksternal

print(3 * "=", "Membaca file txt", 3 * "=")
file = open("data.txt",mode = "w")

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")


#print(file.read())