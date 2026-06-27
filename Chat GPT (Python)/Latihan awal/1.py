import os
os.system("cls")
import pandas as pd

data = {
    'Nama' : ['fakhri', 'dinal', 'maulana'],
    'Umur' : [17, 16, 18],
    'Hobi' : ['ngoding', 'baca buku', 'nonton']
}

df = pd.DataFrame(data)

print("=== DataFrame")
print(df)

print("\n=== Info Data===")
print(df.info())

print("\n=== Head (5 data pertama)===")
print(df.head())