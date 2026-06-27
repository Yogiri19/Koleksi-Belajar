import os
os.system('cls')

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


x = [ 
    [1,100000],
    [2,200000],
    [3,300000],
    [4,400000],
    [5,500000],
    [6,600000],
    [7,700000],
    [8,800000]
]

y = [0,0,0,1,1,1,1,1]
x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.25, random_state=42
)

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = KNeighborsClassifier(n_neighbors=3)

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print(f"Prediksi: {y_pred}")
print(f"asli: {y_test}")

acc = accuracy_score(y_test,y_pred)

print(f"accuracy: {acc}")

prediksi_baru = scaler.transform([[4,450000]]) # fit_transform() -> mengubah data
hasil = model.predict(prediksi_baru)

print(f"prediksi data baru: {hasil}")