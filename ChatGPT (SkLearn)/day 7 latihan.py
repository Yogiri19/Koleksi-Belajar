import os
os.system("cls")

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# Soal Pertama
x = [
    [1],[2],[3],[4],[5]
]
y = [0,0,0,1,1]

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.2
)
model = KNeighborsClassifier(n_neighbors=1)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
print(f"Prediksi: {y_pred}")
print(f"Asli: {y_test}")

# Soal Kedua
y = [
    [1,1000],
    [2,2000],
    [3,3000],
    [4,4000],
    [5,5000]
]
y = [0,0,0,1,1]

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.4
)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

acc = accuracy_score(y_test,y_pred)

print(f"Prediksi: {y_pred}")
print(f"Asli: {y_test}")
print(f"accuracy: {acc}")

# Soal Ketiga
x = [
    [10,50000],
    [20,60000],
    [30,70000],
    [40,80000],
    [50,90000],
    [60,100000]
]
y = [0,0,0,1,1,1]

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.33
)

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train,y_train)

data_baru = scaler.transform([[35,75000]])
hasil = model.predict(data_baru)
print(f"data Baru: {hasil}")

# Soal keempat
x = [
    [1,2],
    [3,4],
    [3,4],
    [5,6],
    [7,8],
    [8,9]
]
y = [0,0,0,1,1,1]

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.33
)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model1 = KNeighborsClassifier(n_neighbors=1)
model2 = KNeighborsClassifier(n_neighbors=3)

model1.fit(x_train,y_train)
y_pred1 =  model1.predict(x_test)

model2.fit(x_train,y_train)
y_pred2 = model2.predict(x_test)


acc1 = accuracy_score(y_test,y_pred1)
acc2 = accuracy_score(y_test,y_pred2)

print(f"Accuracy k=1: {acc1}")
print(f"Accuracy k=3: {acc2}")

# Soal Kelima
x = [
    [18,2],
    [20,2],
    [22,4],
    [40,7],
    [42,8],
    [45,9],
    [50,10],
    [55,11]
]
y = [0,0,0,1,1,1,1,1]

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.25
)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
acc = accuracy_score(y_test,y_pred)

print(f"Accuracy: {acc}")

prediksi_baru = scaler.transform([[25,5]])
hasil = model.predict(prediksi_baru)

print(f"Accuracy: {acc}")
print(f"Prediksi data baru: {hasil}")