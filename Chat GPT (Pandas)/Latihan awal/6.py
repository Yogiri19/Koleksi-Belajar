import os
os.system("cls")

import pandas as pd
pd.set_option('display.max_columns', None)

data = {
    'Nama' : ['fakhri', 'dinal', 'maulana'],
    'Umur' : [17, 16, 18],
    'Hobi' : ['ngoding', 'baca', 'nonton']
}

df = pd.DataFrame(data)
print("=== DATA ===")
print(df, "\n")

# 1. Rata-rata umur
print("=== RATA-RATA UMUR ===")
print(df['Umur'].mean(), "\n") # dijumlahkan lalu / 3

# 2. Umur terkecil & terbesar
print("=== UMUR TERKECIL ===") # nilai terkecil
print(df['Umur'].min())

print("=== UMUR TERBESAR ===")
print(df['Umur'].max(), "\n") # nilai terbesar

# 3. Jumlah total umur
print("=== TOTAL UMUR ===")
print(df['Umur'].sum(), "\n") # jumlahkan semua

# 4. Jumlah data
print("=== JUMLAH DATA UMUR ===")
print(df['Umur'].count(), "\n") # jumblahkan data

# 5. Statistik lengkap
print("=== DESCRIBE ===")
print(df['Umur'].describe(), "\n") 

# 6. Hitung kategori
print("=== JUMLAH HOBI ===")
print(df['Hobi'].value_counts())
