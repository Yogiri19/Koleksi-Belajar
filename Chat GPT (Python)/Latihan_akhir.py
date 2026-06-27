import os
os.system("cls")
import pandas as pd
pd.set_option('display.max_columns', None)

data = {
    'Nama' : ['Andi', 'Budi', 'Cici', 'Dodi', 'Eka', 'Fani'],
    'Umur' : [17, 18, None, 17, 19, None],
    'Nilai' : [80, 75, 90, None, 85, 70],
    'Kelas' : ['A', 'A', 'B', 'B', 'A', 'B']
}

df = pd.DataFrame(data)
print("\n===Soal pertama")
print(df.head())

print("\n===Soal kedua")
print(df.isna().sum())

print("\n===Soal Ketiga")
print(df[['Nama', 'Nilai']])

print("\n===Soal Keempat")
print(df['Umur'].mean())

print("\n===Soal Kelima")
df['Nilai'] = df['Nilai'].fillna(df['Nilai'].mean())
print(df['Nilai'])

print("\n=== Soal Keenam")
print(df[df['Nilai'] >= 80])

print("\n=== Soal Ketujuh")
print(df['Kelas'].value_counts())

print("\n=== Soal kedelapan")
print(df.groupby('Kelas')['Nilai'].mean())

print("\n===Saol Kesembilan")
df.sort_values(by ='Nilai',ascending = False)
print(df)
print("\n=== Soal Kesepuluh")
df['Status'] = df['Nilai'].apply(
    lambda u: 'Lulus' if u >= 80 else 'Tidak Lulus'
)
print(df)