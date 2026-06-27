import os
os.system('cls')

import pandas as pd

pd.set_option('display.max_columns', None)
# 1. Membuat DataFrame dari dictionary
data = {
    'Nama' : ['Fakhri', 'dinal', 'maulana'],
    'Umur' : [17, 16, 18],
    'Hobi' : ['Ngoding', 'baca buku', 'nonton']
}

df = pd.DataFrame(data)
print("=== Data Awal ===")
print(df, '\n')

# 2. Memilih kolom
print(" === Pilih Kolom Nama ===")
print(df['Nama'], "\n")

print("=== Pilih Kolom Nama & Umur ===")
print(df[['Nama', 'Umur']], "\n")

print("=== Pilih Kolom Nama & Umur & Hobi ===")
print(df[['Nama', 'Umur', 'Hobi']], "\n")

# 3. Memilih Baris
print("=== Baris Pertama (loc) ===")
print(df.loc[0], "\n")

print("=== Baris Kedua (iloc) ===")
print(df.iloc[1,0], "\n")

# 4. Filter baris
print("=== Filter: Umur > 17 ===")
print(df[df['Umur'] > 17], "\n")

# 5. Tambah Kolom Baru
df['Status'] = 'Pelajar'
print("=== Tambah Kolom Status ===")
print(df, "\n")


# 6. Hapus Kolom
df = df.drop('Status', axis = 1)
print("=== Hapus kolom Status")
print(df, "\n")

# 7. Sort data berdasarkan umur
print("=== Urutkan Berdasarkan Umur ===")
print(df.sort_values('Umur'))
