import os
os.system('cls')

import pandas as pd
pd.set_option('display.max_columns', None)

df_siswa = pd.DataFrame({
    'ID' : [101, 102, 103],
    'Nama' : ['Andi', 'Budi', 'Citra'],
    'Umur' : [17, 18, 17]
})

df_siswa_baru = pd.DataFrame({
    'ID' : [104],
    'Nama' : ['Dewi'],
    'Umur' : [18]
})

df_nilai = pd.DataFrame({
    'ID' : [101, 102, 103],
    'Nilai' : [85, 90, 88]
})

df_status = pd.DataFrame({
    'ID' : [101, 102, 104],
    'Status' : ['Pelajar', 'Pelajar', 'Pelajar']
})
print("=== soal pertama")
df_concat = pd.concat([df_siswa, df_siswa_baru], ignore_index=True)
print(df_concat)

print("=== Soal Kedua")
df_concat_kolom = pd.concat([df_siswa, df_nilai], axis=1)
print(df_concat_kolom)

print("=== Soal Ketiga")
df_merge = pd.merge(df_siswa, df_status, on='ID')
print(df_merge)

print("=== Soal Keempat")
df_temp = pd.merge(df_siswa, df_nilai, on ='ID', how='left')
df_final = pd.merge(df_temp, df_status, on='ID', how='left')
print(df_final)