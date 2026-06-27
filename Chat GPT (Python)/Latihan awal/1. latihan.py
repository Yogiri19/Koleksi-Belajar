import os
os.system("cls")

import pandas as pd

# data = {
#     'Nama' : ['Fakhri', 'Yogiri' ],
#     'Umur' : [14, 17] 
# }

# df = pd.DataFrame(data)

# print(df)

# data = {
#     'Nama' : ['Fakhri'],
#     'Nilai UAS' : ['50'],
#     'Nilai UTS' : ['30']
# }
# df = pd.DataFrame(data)
# print(df)
# print("== menggunakan info==")

# print(df.info())


data = {
    'Nama' : ['fakhri', 'dinal', 'maulana'],
    'Umur' : [17, 16, 18],
    'Hobi' : ['ngoding', 'baca buku', 'nonton']
}
df = pd.DataFrame(data)
print("\n ===Ini adalah head===")
print(df.head())
print("\n ===Ini adalah info===")
print(df.info())

print("\n ===Ini adalah upper===")
df['Nama'] = df['Nama'].str.upper()
print(df)
df['Umur'] = df['Umur'] + 1
print(df)
