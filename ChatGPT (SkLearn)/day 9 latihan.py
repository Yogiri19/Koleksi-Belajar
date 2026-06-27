import os
os.system("cls")

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

# Soal pertama
x = [
    [1],[2],[3],[4],[5]
]
y = [0,0,0,1,1]
x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.2
)
model = RandomForestClassifier(n_estimators=5, max_depth=2)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
print(f"Prediksi: {y_pred}")
print(f"Asli: {y_test}")

# Soal kedua
x = [
    [10,50],
    [20,55],
    [30,60],
    [40,65],
    [50,70],
    [60,75]
]
y = [0,0,0,1,1,1]
x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.33
)
model = RandomForestClassifier(n_estimators=10, max_depth=3)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

acc = accuracy_score(y_test,y_pred)

print(f"Prediksi: {y_pred}")
print(f"Asli: {y_test}")
print(f"Accuracy: {acc}")

# Soal Ketiga
x = [
    [5,100],
    [10,200],
    [15,300],
    [20,400],
    [25,500],
    [30,600]
]
y = [0,0,0,1,1,1]
x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.33
)
model = RandomForestClassifier(n_estimators=10, max_depth=2)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
acc = accuracy_score(y_test,y_pred)
cm = confusion_matrix(y_test,y_pred)

print(f"Accuracy: {acc}")
print(f"Confusion Matrix: {cm}")

# Soal Keempat

x = [
    [1,10],
    [2,20],
    [3,30],
    [4,40],
    [5,50],
    [6,60],
    [7,70],
    [8,80]
]
y = [0,0,0,0,1,1,1,1]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.25
)
model1 = RandomForestClassifier(n_estimators=5)
model2 = RandomForestClassifier(n_estimators=20)
model1.fit(x_train,y_train)
model2.fit(x_train,y_train)

y_pred1 = model1.predict(x_test)
y_pred2 = model2.predict(x_test)

acc1 = accuracy_score(y_test,y_pred1)
acc2 = accuracy_score(y_test,y_pred2)

print(f"Accuracy 5 tree: {acc1}")
print(f"Accuracy 20 tree: {acc2}")

# Soal Kelima
x = [
    [18,60],
    [20,65],
    [22,70],
    [25,75],
    [30,80],
    [35,85],
    [40,90],
    [45,95]
]
y = [0,0,0,1,1,1,1,1]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.25
)
model = RandomForestClassifier(n_estimators=10, max_depth=3)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
acc = accuracy_score(y_test,y_pred)
cm = confusion_matrix(y_test,y_pred)

prediksi_baru = model.predict([[23,72]])

print(f"Accuracy: {acc}")
print(f"Confusion Matrix: {cm}")
print(f"Prediksi data baru: {prediksi_baru}")