import os
os.system("cls")

import pandas as pd
pd.set_option("display.max_columns", None)

df = pd.DataFrame({
    'Nama' : ['fakhri', 'dinal', 'Maulana'],
    'Kelas' : ['a', 'b', 'c']
})
print(df)