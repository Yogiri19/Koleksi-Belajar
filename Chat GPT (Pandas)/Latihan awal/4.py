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
print("===DATA AWAL=== ")
print(df)

# 1. SORTING DATA
print("\n=== SORT Umur (Kecil -> Besar) ===")
print(df.sort_values('Umur')) # Kenapa dari kecil ke besar? 
                            # karena defaultnya Ascending = True
# Sama seperti                
df = df.sort_values('Umur')
print(df)
print(df.sort_values('Umur', ascending=True))

print("\n === SORT Umur (Besar -> kecil) ===")
print(df.sort_values('Umur', ascending=False))

print("\n=== SORT Nama (A -> Z) ===")
print(df.sort_values('Nama'))

print("\n=== SORT Nama (Z -> A) ===")
print(df.sort_values('Nama', ascending=False))

# 2. COUNTING (values_counts)
print("\n=== HITUNG JUMLAH HOBI===")
print(df['Hobi'].value_counts())
print("\n=== HITUNG JUMLAH UMUR===")
print(df['Umur'].value_counts())
print("\n=== HITUNG JUMLAH NAMA")
print(df['Nama'].value_counts())

# 3. COUNTING -> DATAFRAME
print("\n=== HOBI KE DATAFRAME===")
hobi_df = df['Hobi'].value_counts().reset_index()
hobi_df.columns = ['Hobi', 'Jumlah']
print(hobi_df)

print("\n=== UMUR KE DATAFRAME===")
umur_df = df['Umur'].value_counts().reset_index()
umur_df.columns = ['Umur', 'jumlah']
print(umur_df)

# 4. CATATAN PENTING
print("=== CATATAN===")
print("- sort_values() = tidak mengubah df asli")
print("- value_counts() = menghilangkan frekuensi data")
print("- reset_index() merapikan hasil menjadi DataFrame")
