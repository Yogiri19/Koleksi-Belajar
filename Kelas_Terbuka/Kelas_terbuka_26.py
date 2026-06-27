#continue, pass, break

#pass -> dia berfungsi sebagai dummy (Tidak akan di eksekusi)

# angka = 0

# while angka < 5:
#     angka += 1
    
#     if angka == 3:
#         pass # Ini tidak akan dieksekusi, akan dilakukan di luar blok selanjutnya
    
#     print(angka)

angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") # aksi 1
    if angka == 3:
        print("jawaban")
        continue # akan membuat loop meloncat ke step selanjutnya 
    print("contoh") # aksi 2
print("finish!")


