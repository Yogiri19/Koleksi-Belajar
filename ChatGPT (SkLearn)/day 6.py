import os
os.system('cls')

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

x = [[1],[2],[3],[4],[5],[6],[7],[8]]
y = [0,0,0,1,1,1,1,1]

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.25, random_state=42
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
print(f"data test: {x_test}")
print(f"nilai asli: {y_test}")
print(f"prediksi: {y_pred}")

acc = accuracy_score(y_test,y_pred)
print(f"accuracy: {acc}")

cm = confusion_matrix(y_test,y_pred)
print(f"Confusion: {cm}")

prediksi_baru = model.predict([[4]])
print(f"Prediksi baru: {prediksi_baru}")