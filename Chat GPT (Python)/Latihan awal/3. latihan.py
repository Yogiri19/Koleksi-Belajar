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
print(df)

df['Umur+1'] = df['Umur'].apply(
    lambda u: u + 1 
)
print(f'=== INI n + 1 \n{df}\n')

df['Status'] = df['Umur'].apply(
    lambda u: 'Dewasa' if u >= 18 else 'Pelajar'
)
print(f'===INI Status \n{df}\n')


df['Hobi_Panjang'] = df['Hobi'].apply(
    lambda h: 'Panjang' if len(h) >= 5 else 'Pendek'
)
print(f"=== Hobi_Panjang \n{df}\n")