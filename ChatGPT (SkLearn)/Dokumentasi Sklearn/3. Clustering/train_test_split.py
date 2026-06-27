import os
os.system('cls')

from sklearn.model_selection import train_test_split
# Fungsinya membagi 2 data -> train dan test

# Contoh datanya
x = [[1],[2],[3],[4],[5]]
y = [2,4,6,8,10]

# Polosan
x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.2 # 20% test, 80% train & hasilnya random
)
print(f"x_train: {x_train}")
print(f"x_test: {x_test}")

# Menggunakan random_state
x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.2, random_state=42 # hasilnya akan konsisten
)
print(f"\nx_train: {x_train}")
print(f"x_test: {x_test}")


# Contoh data 2
x = [[1],[2],[3],[4],[5]]
y = [0,0,1,1,1]

# Parameter keren
x_train,x_test,y_train,y_test = train_test_split(
    x,y,
    test_size=0.4,
    random_state=42,
    shuffle=True, # datanya diacak dulu sebelum dibagi
    stratify=y # agar train dan test di samakan
)
print(f"\nx_train: {x_train}")
print(f"x_test: {x_test}")

# berarti shuffle x nya yang di acak