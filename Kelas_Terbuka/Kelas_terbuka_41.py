# copy dictionary

teman_teman = {
    "ri" : "fakhri",
    "nal" : "dinal"
}

friends = teman_teman.copy()

print(f"teman-teman = {teman_teman}\n")
print(f"friends = {friends}\n")
teman_teman["na"]="maulana" 
print(f"teman-teman = {teman_teman}\n")
print(f"friends = {friends}\n")

# pop dictionary ( memisahkan dictionary)
dataDinal = friends.pop("nal")
print(f"data dinal = {dataDinal}\n")
print(f"friends = {friends}\n")

# popitem dictionary #(item itu key dan valuenya)
print("=====")
dataterakhir = friends.popitem()
print(f"data terakhir = {dataterakhir}\n")
print(f"friends = {friends}\n")