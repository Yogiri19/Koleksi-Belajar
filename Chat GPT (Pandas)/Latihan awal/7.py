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

# 1. Group berdasarkan Hobi
print("=== GROUP BY HOBI ===")
print(df.groupby('Hobi'), "\n")

# 2. Hitung jumlah orang per hobi
print("=== JUMLAH PER HOBI ===")
print(df.groupby('Hobi').size(), "\n")

# 3. Rata-rata umur per hobi
print("=== RATA-RATA UMUR PER HOBI ===")
print(df.groupby('Hobi')['Umur'].mean(), "\n")

# 4. Banyak agregasi sekaligus
print("=== AGREGASI ===")
print(df.groupby('Hobi')['Umur'] # Imi kelompokan berdasarkan Hobi, Lalu hitung rata-rata umur
      .agg(['min', 'max', 'mean', 'count'])
)
