import os
os.system('cls')

import pandas as pd
pd.set_option('display.max_columns',None)

data = {
    'Nama' : ['fakhri', 'dinal', 'maulana'],
    'Umur' : [17, 16, 18],
    'Hobi' : ['ngoding', 'baca', 'nonton']
}

df = pd.DataFrame(data)
# print("Ini data normal")
# print(df)
# print("\n=== Soal Pertama")
# df['Nama'] = df['Nama'].str.capitalize()
# df['Hobi'] = df['Hobi'].str.lower()
# print(df)

# print("\n=== Ini soal kedua")
# df['Nama_panjang'] = df['Nama'].apply(
#     lambda n: len(n)
# )
# print(df)

# print("\n=== Soal ketiga")
# df['Nama'] = df['Nama'].str.capitalize()
# df['Hobi'] = df['Hobi'].str.upper()

# df['Status']= df['Umur'].apply(
#     lambda u: 'Dewasa' if u >= 18 else 'Pelajar'
# )
# print(df)

# print("\n=== Soal pertama")
# df['Nama'] = df['Nama'].str.upper()
# df['Hobi'] = df['Hobi'].str.capitalize()
# print(df)

# print("\n=== soal kedua")
# df['Kategori_umur'] = df['Umur'].apply(
#     lambda u: 'Anak' if u < 17 else
#     'remaja' if u <= 18 else
#     'Dewasa'
# )
# print(df)

# print("\n=== soal ketiga")
# df['Nama'] = df['Nama'].str.capitalize()
# df['Panjang_Hobi'] = df['Hobi'].apply(
#     lambda h: len(h)
# )
# df['Status'] = df['Umur'].apply(
#     lambda u: 'Dewasa' if u >= 18 else 'Pelajar'
# )
# print(df)

# print("\n=== Soal pertama")
# df['Umur_status'] = df['Umur'].apply(
#     lambda u: 'Genap' if ((u % 2) == 0) else 'Ganjil'
# )
# print(df)

# print("\n=== soal 2")
# df['Hobi_Jenis'] = df['Hobi'].apply(
#     lambda h: 'Panjang' if len(h) >= 6 else 'Pendek'
# )
# print(df)

# print("\n=== soal ketiga")
# df['Level'] = df['Umur'].apply(
#     lambda u: 'Anak' if u < 17 else
#     'Remaja' if u >= 17 else
#     'Dewasa'
# )
# print(df)
#=========================================
# print("\n=== soal pertama")
# df['Umur_status'] = df['Umur'].apply(
#     lambda u: 'Ganjil' if u % 2 else 'Genap'
# )
# df['Umur_status'] = df['Umur_status'].replace({
#     'Ganjil' : 'Odd',
#     'Genap' : 'Even'
# })
# print(df)

# print("\n=== Soal Kedua")
# df['Hobi_jenis'] = df['Hobi'].apply(
#     lambda h: 'Panjang' if len(h) >= 6 else 'Pendek'
# )
# df['Hobi_jenis'] = df['Hobi_jenis'].replace('Panjang', 'Long')
# df['Hobi_jenis'] = df['Hobi_jenis'].replace('Pendek', 'Short')
# print(df)

# print("\n=== soal ketiga")
# df['Level'] = df['Umur'].apply(
#     lambda u: 'Anak' if u < 17 else
#     'Remaja' if u >= 17 else
#     'Dewasa'
# )
# df['Level'] = df['Level'].replace('Anak', 'Child')
# df['Level'] = df['Level'].replace('Remaja', 'Teen')
# df['Level'] = df['Level'].replace('Dewasa', 'Adult')
# print(df)

# print("\n=== Soal Keempat")
# df['Umur'] = df['Umur'].replace({18:19, 20:21})
# print(df)

#==========================
# print("=== Soal pertama")
# df = df.rename(columns={'Umur': 'Usia'})
# print(df)
# print("\n=== Soal Kedua")
# df = df.rename(columns={'Nama' : 'Nama_Lengkap',
#                         'Hobi' : 'Kegiatan'})
# print(df)
# print("\n=== Soal Ketiga")
# df_baru = df.rename(columns={'Nama_Lengkap' : 'NAMA',
#                         'Usia' : 'USIA'})
# print("DF ASLI")
# print(df)
# print("\nDF BARU")
# print(df_baru)

#======================================
# print("===Soal Pertama")
# df = df.rename(columns={'Nama' : 'nama',
#                         'Umur' : 'usia'})
# print(df)
# print("\n===Soal Kedua")
# df_2 = df.rename(columns={'Hobi' : 'Kegiatan',
#                           'usia' : 'USIA'})
# print(f"df asli\n {df}")
# print(f"df_2 \n {df_2}")
# print("\n=== Soal Ketiga")
# df_3 = df_2.columns.str.upper()
# print(df_3)
# df_3 = df_2.copy() # memakai copy agar df_2 nya tidak berubah
# df_3.columns = df_3.columns.str.upper()
# print(df_3)

print("\n===Soal pertama")
df_1 = df.copy()
df_1 = df_1.drop('Hobi', axis=1)
print(df_1)

print("\n=== Soal Kedua")
df_2 = df.copy()
df_2 = df_2.drop('Umur', axis=1)
print(f"\n{df}")
print(f"\n{df_2}")

print("\n=== Soal Ketiga")
df_3 = df_2.copy()
df_3 = df_3.drop(['Nama', 'Hobi'], axis=1)
print(df_3)
# df.drop(columns=['A', 'B'])
# df.drop(['A', 'B'], axis=1)
