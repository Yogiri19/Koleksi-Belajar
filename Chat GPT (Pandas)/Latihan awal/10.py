import os
os.system('cls')

import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.DataFrame({
    'Nama' : ['fakhri', 'dinal', 'maulana'],
    'Umur' : [17, 16, 18],
    'Hobi' : ['ngoding', 'baca', 'nonton']
})
print("=== df biasa")
print(df)

print("\n=== Apply Angka")
df['Umur_Tahun_Depan'] = df['Umur'].apply(
    lambda u: u + 1)
print(df)

print("\n=== Apply Kondisi")
df['Status'] = df['Umur'].apply(
    lambda u: 'Dewasa' if u >= 18 else 'Pelajar'
)
print(df)

print("\n=== Apply string")
df['Nama_Capital'] = df['Nama'].apply(lambda n: n.capitalize())
df['Hobi_Upper'] = df['Hobi'].apply(lambda h: h.upper())
print(df)

print("\n=== Apply Multi Logic")
def kategori_umur(u):
    if u < 17:
        return 'Anak'
    elif u < 18:
        return 'Remaja'
    else:
        return 'Dewasa'
df['Kategori_Umur'] = df['Umur'].apply(kategori_umur)
print(df)