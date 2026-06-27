# looping dictionary

teman_teman = {
    "ri" : "fakhri",
    "nal" : "dinal",
    "na" : "maulana",
}

# looping first try

for teman in teman_teman: # yang keluar adalah key nya
    print(teman)

print("===========") 
# operator untuk mengambil item / iterables
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))
print("===========") 

values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)
print("===========") 

items = teman_teman.items()
print(items)

for item in teman_teman.items():
    print(item)

for key, value in teman_teman.items():
    print(f"key = {key}, value = {value}")    

