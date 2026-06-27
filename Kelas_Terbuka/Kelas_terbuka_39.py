# operator dictionary

data_dict = {
    "ri" : "fakhri"
}

# panjang dictionary
lendict = len(data_dict) # menghitung dari 0
print(f"panjang dictonary: {lendict}")

# mengecek key exist atau tidak
key = "ri"
cek = key in data_dict
print(f"apakah {key} ada di data_dict: {cek} ")

# mengakses value dengan get, menggunakan key
print("=====gets=====")
print(data_dict["ri"]) # cara 1
print(data_dict.get("ri")) # cara 2
print(data_dict.get("kis")) # agar tidak muncul eror, mencari key yang tidak ada
print(data_dict.get("kis", "key tidak ditemukan")) # menambahkan string

# mengupdate update(mengganti dict)
print("=====UPDATE=====")
data_dict["nal"] = "dinal"
print(data_dict)
data_dict.update({"nal" : "dinal"}) # jika sudah ada, dia tidak akan menambahkan
print(data_dict) 
data_dict.update({"na":"maulana"}) # kalo gak ada di add aja di belakang
print(data_dict)

del data_dict["na"]
print(data_dict)




