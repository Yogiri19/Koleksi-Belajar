import os
os.system('cls')

import pandas as pd
pd.set_option('display.max_columns', None)

data = {
    'Nama' : ['fakhri', 'dinal', 'maulana'],
    'Umur' : [17, 16, 18],
    'Hobi' : ['Ngoding', 'baca', 'nonton']
}
df = pd.DataFrame(data)
print(f"=== Ini df biasa ")
print(df)
print(f"\n=== ini df.groupby('Hobi')")
print(df.groupby('Hobi'))
print(f"\n=== Ini df.groupby('Hobi').size()")
print(df.groupby('Hobi').size())
print(f"\n=== ini df.groupby('Hobi)['Umur].mean()")
print(df.groupby('Hobi')['Umur'].mean())
print(df.groupby('Hobi')['Umur'].agg(['min', 'max', 'mean', 'count']))

