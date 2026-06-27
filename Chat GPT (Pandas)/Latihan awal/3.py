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

print("=== DATA AWAL ===")
print(df, "\n")

# ===============================
# 1. STRING OPERATION
# ===============================
print("=== STRING OPERATION ===")

df['Nama'] = df['Nama'].str.capitalize()
df['Hobi'] = df['Hobi'].str.upper()

print(df, "\n")

# ===============================
# 2. CEK TIPE DATA
# ===============================
print("=== INFO DATA ===")
print(df.info(), "\n")

# ===============================
# 3. TAMBAH KOLOM DARI KOLOM LAIN (apply + lambda)
# ===============================
print("=== TAMBAH KOLOM STATUS ===")

df['Status'] = df['Umur'].apply(
    #Hasil_Jika_True if KONDISI else HASIL_JIKA_FALSE
    lambda u: 'Dewasa' if u >= 18 else 'Pelajar'
)
print(df, "\n")

# ===============================
# 4. MAPPING / REPLACE NILAI
# ===============================
print("=== MAPPING HOBI ===")

map_hobi = {
    'NGODING': 'Coding',
    'BACA': 'Membaca',
    'NONTON': 'Menonton'
}

df['Hobi_Rapi'] = df['Hobi'].map(map_hobi)

print(df, "\n")

# ===============================
# 5. SORT + RESET INDEX
# ===============================
print("=== SORT BERDASARKAN UMUR ===")

df_sorted = df.sort_values('Umur').reset_index(drop=True)
print(df_sorted, "\n")

# ===============================
# 6. LATIHAN DAY 3 (CONTOH JAWABAN)
# ===============================
print("=== LATIHAN DAY 3 ===")

# Soal 1: Nama jadi HURUF BESAR
df['Nama_Besar'] = df['Nama'].str.upper()

# Soal 2: Kelompok umur
df['Kelompok'] = df['Umur'].apply(
    lambda u: 'Remaja' if u < 18 else 'Dewasa'
)

# Soal 3: Kode = huruf awal nama + "-" + umur
df['Kode'] = df['Nama'].str[0] + "-" + df['Umur'].astype(str)

print(df)
