# Latihan kalkulator
# kalkulator sederhana
# print(20*"=")
# print("Kalkulator Sederhana")
# print(20*"=" + "\n")
angka_1 = float(input("Masukan angka 1 = "))
operator = input("operator (+, -, *, /) :")
angka_2 = float(input("Masukan angka 2 = "))

# Percabangan 
if operator == "+":
    hasil = angka_1 + angka_2
    print (f" pertambahan {angka_1} dan {angka_2} adalah = {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print (f" pengurangan {angka_1} dan {angka_2} adalah = {hasil}")
elif operator == "*":
    hasil = angka_1 * angka_2
    print (f" pengkalian {angka_1} dan {angka_2} adalah = {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print (f" pembagian {angka_1} dan {angka_2} adalah = {hasil}")
else:
    print("Dasar tolol, masukin yang benar")   
print("itulah kakulator sederhana")