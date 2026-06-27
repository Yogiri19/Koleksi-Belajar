import os
os.system('cls')

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

x = [
    [1,50],
    [2,55],
    [3,60],
    [4,65],
    [5,70],
    [6,75],
    [7,80],
    [8,85],
    [2,50],
    [3,55],
    [6,80],
    [7,85]
]

y = [0,0,0,1,1,1,1,1,0,0,1,1]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.25, random_state=42
)
model = RandomForestClassifier(n_estimators=20, max_depth=4)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print(f"data test: {x_test}")
print(f"data asli: {y_test}")
print(f"Prediksi: {y_pred}")

acc = accuracy_score(y_test,y_pred)
print(f"Accuracy Score: {acc}")

cm = confusion_matrix(y_test,y_pred)
print(f"Confusion matrix: {cm}")

data_baru = [[5,72]]
hasil = model.predict(data_baru)

print(f"Prediksi data baru (0=tidak,1=lulus): {data_baru}")

