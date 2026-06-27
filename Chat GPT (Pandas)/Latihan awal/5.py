import os
os.system("cls")
import pandas as pd
pd.set_option('display.max_columns', None)

# Data tetap (sesuai permintaanmu)
data = {
    'Nama' : ['fakhri', 'dinal', 'maulana'],
    'Umur' : [17, 16, 18],
    'Hobi' : ['ngoding', 'baca', 'nonton']
}

df = pd.DataFrame(data)
print("=== DATA AWAL ===")
print(df, "\n")

# 1. Ubah format teks
print("=== SETELAH FORMAT TEKS ===")
df['Nama'] = df['Nama'].str.capitalize() # huruf pertama kapital
df['Hobi'] = df['Hobi'].str.upper() # semua kolom kapital
print(df, "\n")

# 2. Ganti nilai tertentu
print("=== SETELAH REPLACE ===")
df['Hobi'] = df['Hobi'].replace('BACA', 'MEMBACA')

print(df, "\n")

# 3. Rename kolom
print("=== SETELAH RENAME KOLOM ===")
df = df.rename(columns={'Umur': 'Usia'})

print(df, "\n")

# 4. Tambah kolom Status
print("=== TAMBAH KOLOM STATUS ===")
df['Status'] = df['Usia'].apply(
    lambda u: 'Dewasa' if u >= 18 else 'Pelajar'
)

print(df, "\n")

# 5. Hapus kolom
print("=== SETELAH HAPUS KOLOM STATUS ===")
df = df.drop('Status', axis=1)

print(df)
