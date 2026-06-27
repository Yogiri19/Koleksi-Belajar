import os
os.system('cls')

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

x = [
    [1,50], # [kelas\level, nilai]
    [2,55],
    [3,60],
    [4,65],
    [5,70],
    [6,75],
    [7,80],
    [8,85]
]

y = [0,0,0,1,1,1,1,1]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size= 0.25, random_state=42
) 
model = DecisionTreeClassifier(max_depth=3) # Maks kedalaman pohon = 3
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print(f"data test: {x_test}")
print(f"nilai asli: {y_test}")
print(f"Prediksi: {y_pred}")

acc = accuracy_score(y_test,y_pred)
print(f"accuracy: {acc}")

cm = confusion_matrix(y_test,y_pred)
print(f"confusion matrix: {cm}")

prediksi_baru = model.predict([[4,65]])
print(f"prediksi (0=tidak, 1=lulus): {prediksi_baru}")


