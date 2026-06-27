import os
os.system("cls")

import pandas as pd

data = {
    'Nama' : ['fakhri', 'dinal', 'maulana'],
    'Umur' : [17, 16, 18],
    'Hobi' : ['ngoding', 'baca', 'nonton']
}
df = pd.DataFrame(data)

print(df)
print("\n=== ini 1")
print(df.loc[1])
print("\n=== ini 2")
print(df.loc[[0,2], ['Nama', 'Hobi']])

print("\n=== pake iloc [2,0]")
print(df.iloc[2,0])
print("\n=== Umur > 17")
print(df[df['Umur'] > 17])

# Dimulai dari sini CUKKK

print("\n=== Ini Hobi = 'ngoding' DAN Umur > 17 ===")
print(df[(df['Hobi'] == 'ngoding') & (df['Umur'] > 17)])

# ini contoh 1
print("\n=== Umur < 18 ATAU Nama == 'dinal' DAN Hobi = 'baca'===")
print(df[(df['Umur'] < 18) | (df['Nama'] == 'dinal') & (df['Hobi'] == 'baca')])

# ini contoh 2
print("\n=== (Umur < 18) ATAU (Nama == 'fakhri' DAN  Hobi = 'baca')===")
print(df[(df['Umur'] < 18) & ((df['Nama'] == 'fakhri') | (df['Hobi'] == 'baca'))])

# df['Status'] = 'Pelajar'
# print("=== Ini Soal 1 ===\n")
# print(df)

# df['Lulus'] = df['Nilai'].apply(lambda n: 'Lulus' if n >= 75 else 'Tidak')






