# concat = gabungan
# merge = menggabungkan 
import os
os.system('cls')

import pandas as pd
pd.set_option('display.max_columns', None)

data = {
    'Nama' : ['fakhri', 'dinal', 'maulana'],
    'Umur' : [17, 16, 18],
    'Hobi' : ['ngoding', 'baca', 'nonton']
}

df = pd.DataFrame(data)
print("=== DF UTAMA ===")
print(df, "\n")


df_baru = pd.DataFrame({
    'Nama' : ['rizal'],
    'Umur' : [20],
    'Hobi' : ['ngoding']
})

df_concat_row = pd.concat([df, df_baru], ignore_index=True) # ini True agar berurutan

print("=== CONCAT ROW (TAMBAH BARIS) ===")
print(df_concat_row, "\n")

df_nilai = pd.DataFrame({
    'Nilai' : [80, 75, 90]
})

df_concat_col = pd.concat([df, df_nilai], axis=1)

print("=== CONCAT COLUMN (TAMBAH KOLOM) ===")
print(df_concat_col, "\n")

df_status = pd.DataFrame({
    'Nama' : ['fakhri', 'dinal', 'maulana'],
    'Status' : ['Pelajar', 'Pelajar', 'Dewasa']
})

print("=== DF STATUS ===")
print(df_status, "\n")

df_merge = pd.merge(df, df_status, on='Nama')
print("=== HASIL MERGE ===")
print(df_merge, "\n")
