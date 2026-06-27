import os
os.system('cls')

import pandas as pd
pd.set_option('display.max_columns', None)

data = {
    'Nama' : ['fakhri', 'dinal', 'maulana', 'rizal'],
    'Umur' : [17, None, 18, None],
    'Hobi' : ['ngoding', None, 'nonton', 'baca']
}

df = pd.DataFrame(data)
print("=== DATA AWAL ===")
print(df, "\n")

print("=== CEK NaN ===")
print(df.isna(), "\n") # kalo NaN berarti True

print("=== JUMLAH NaN PER KOLOM ===")
print(df.isna().sum(), "\n")

df_drop = df.dropna()
print("=== DROP NaN (BARIS) ===")
print(df_drop, "\n")

df_fill = df.copy()

df_fill['Umur'] = df_fill['Umur'].fillna(df_fill['Umur'].mean())
df_fill['Hobi'] = df_fill['Hobi'].fillna('Tidak Diisi')

print("=== FILL NaN ===")
print(df_fill, "\n")

df_drop_hobi = df.dropna(subset=['Hobi'])
print("=== DROP NaN KHUSUS KOLOM HOBI ===")
print(df_drop_hobi, "\n")
