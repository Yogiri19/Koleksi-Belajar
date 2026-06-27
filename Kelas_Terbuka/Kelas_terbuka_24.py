# Perulangan (loop)

# for kondisi:
# aksi
# ini dengan list
angka_list = [0,1,2,3] # ini adalah list
print(angka_list)

for i in angka_list: # {i} akan mengikuti apa yang di list
    print(f"i itu -> {i}")

print("akhir dari program 1/n")

# ini dengan range
angka_range = range(3) # 3 ini ujungnya gak di ambil, 0 nya dihitung

for i in angka_range:
     print(f"i itu -> {i}")
    
print("akhir dari program 2\n")


# # ini dengan range
# angka_range = range(1,3) # koma ini sebagai pembatas 

# for i in angka_range: # Harus di dalam ini untuk ngrloop
#     print(f"i itu -> {i}")
#     print("saya keren ")
# print("akhir dari program 3/n")

# menggunakan string

data_str = "fakhri"

for huruf in data_str:
    print(huruf)

print("akhir dari program 4/n")
