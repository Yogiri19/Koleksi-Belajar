# width and multiline

# Data

data_nama = "Fakhri Dinal"
data_umur = 18
data_tinggi = 167.2
data_nomor_sepatu = 43

# string standart
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu},"
print(10*"="+ "Data String" +10*"=")
print(data_string)

# String multiline(dengan menggunakan enter atau newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print("\n"+10*"="+ "Data String" +10*"=")
print(data_string)

# String multiline (kutip triplets) menggunakan (""" """)

#nama   = {data_nama} 
data_nama = "Fakhri Dinal"
data_tinggi = 167.2
data_string = f"""
nama   = {data_nama:>5} 
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""

print("\n"+10*"="+ "Data String" +10*"=")
print(data_string)





