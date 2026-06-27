# ---LIST---

# Kumpulan data numbers
data_angka = [1,2,3]
print(data_angka)

# Kumpulan data string
data_string = ["fakhri", "dinal",]
print(data_string)

# Kumpulan data boolean
data_boolean = [True,False,True]
print(data_boolean)

# Kumpulan campuran 
data_campuran = [1,"fakhri", True]
print(data_campuran)

# Cara alternatif membuat list
data_range = range(0,10,2) # Range (Start, Stop, Step)
print(data_range)
data_list = list(data_range)
print(data_list)

# Membuat list dengan for loop, list comprehensen
list_pake_for = [i**2 for i in range (0,10)]
print(list_pake_for) 

# Membuat list pake for pake if
list_pake_for_if = [i for i in range (0,10) if i !=5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range (0,10) if i%2 ==0]
print(list_pake_for_if)

list_pake_for_if = [i for i in range (0,10) if i%2 !=0]
print(list_pake_for_if)