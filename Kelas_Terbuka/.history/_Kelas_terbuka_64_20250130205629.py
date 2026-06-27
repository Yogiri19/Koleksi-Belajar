import os
os.system("cls")
## tutorial membaca file eksternal

print(3 * "=", "Membaca file txt", 3 * "=")
file = open("data.txt",mode = "r")

print(f"status read : {file.readable}")


print(file.read())