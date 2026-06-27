# # Break
# angka = 0

# while angka < 5:
#     angka += 1
#     print(f"angka sekarang = {angka}")

#     if angka == 3:
#         print("nice!")
#         break
    
#     print("Halo bang!")
    
# print("udah bang, udah")


# Break
data_int = int(input("hitung sampai = ")) # jika di "inputnya" di kasih minus,
                                            #maka tidak akan ketemu dan akan terus ngeloop

angka = 0

while True:
    angka += 1
    print(f"count = {angka}")

    if angka == data_int:
        print(f"nice!")
        break
    
    print("Halo bang!")
    
print("udah bang, udah")