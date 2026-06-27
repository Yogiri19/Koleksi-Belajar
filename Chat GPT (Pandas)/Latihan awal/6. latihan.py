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
print(df['Umur'].mean())
print(f"Umur terkecil: {df['Umur'].min()}")
print(f"Umur terbesar: {df['Umur'].max()}")
print(df['Umur'].describe())
print(df['Hobi'].value_counts())