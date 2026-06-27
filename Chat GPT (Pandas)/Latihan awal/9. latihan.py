import os
os.system('cls')

import pandas as pd
pd.set_option('display.max_columns', None)

data = {
    'Nama'  : ['Ayu', 'Bima', 'Cici', 'Doni', 'Eka'],
    'Umur'  : [20, None, 22, None, 21],
    'Kota'  : ['Jakarta', 'Bandung', None, 'Surabaya', None],
    'Hobi'  : ['Membaca', None, 'Gaming', None, 'Olahraga']
}

df = pd.DataFrame(data)
print("=== DATA AWAL ===")
print(df, "\n")

print("=== Soal pertama")
print(df.isna())

print("\n=== Soal Kedua")
print(df.dropna())

print("\n=== Soal Ketiga")
print(df['Umur'].mean(), df['Kota'].fillna())