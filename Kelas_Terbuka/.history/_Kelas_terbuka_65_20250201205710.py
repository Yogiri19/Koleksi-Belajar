import os
os.system("cls")
# 1. mode write

# dia akan membuat file baru jika tidak ada
# lalu akan menimpa atau overwrite isinya

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("jon si jhonny")

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("ucup surucup")

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("ketimpa")

# 2. mode append

with open("data_2.txt",'w',encoding="utf-8") as file:
    file.write("jon si jhonny\n")

with open("data_2.txt",'a',encoding="utf-8") as file:
    file.write("ucup surucup")

with open("data_2.txt",'a',encoding="utf-8") as file:
    file.write("tambah lagi dengan append")
