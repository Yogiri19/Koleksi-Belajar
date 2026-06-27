import os
os.system('cls')

import pandas as pd
pd.set_option("display.max_columns", None)

data = {
    'Nama' : ['fakhri', 'dinal', 'maulana'],
    'Umur' : [17, 16, 18],
    'Hobi' : ['ngoding', 'baca', 'nonton']
}

df = pd.DataFrame(data)
print(df,"\n")
# print(df.sort_values('Umur'),"\n")
# print(df.sort_values('Nama', ascending = False), "\n")
# df_umur_desc = df.sort_values('Umur', ascending = False)
# print(df_umur_desc)
# print(df['Hobi'],"\n")
# print(df.value_counts("Umur"),"\n")
# print(df['Umur'].value_counts())
print(df['Umur'].sort_index())

print("\n === Umur.value_counts()")
print(df['Umur'].value_counts(),"\n")

print("\n === Umur.value_counts().sort_index()")
print(df['Umur'].value_counts().sort_index())

print("\n === Hobi.value_counts(normalize = True) * 100")
print(df['Hobi'].value_counts(normalize = True) * 100)

print("\n === Hobi.value_counts(dropna = False)")
print(df['Hobi'].value_counts(dropna=True))