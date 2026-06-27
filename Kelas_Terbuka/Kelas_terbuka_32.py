# Teknik menduplikat list

a = ["ucup","otong","dudung"]

b = a # pass by reference

# merubah member dari a dan merubah kedua list
a[1] = "michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# addreas dari kedua list
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# mendupikat list dengan menggunakan copy
c = a.copy() # full duplikat / data baru

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")


print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 0 ")
c[0] = "dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 1 ")
a[0] = "otong"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")


