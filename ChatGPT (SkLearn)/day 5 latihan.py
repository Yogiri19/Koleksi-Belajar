import os
os.system('cls')

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Soal Pertama
x = [[1],[2],[3],[4],[5]]
y = [0,0,0,1,1]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.2, 
)
model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

acc = accuracy_score(y_test,y_pred)

cm = confusion_matrix(y_test,y_pred)
print(f"x_test: {x_test}")
print(f"y_test: {y_test}")
print(f"y_pred: {y_pred}")
print(f"accuracy: {acc}")
print(f"confusion matrix: {cm}")

# Soal Kedua
x = [[2],[4],[6],[8],[10],[12]]
y = [0,0,0,1,1,1]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.33, random_state=1
)
model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

acc = accuracy_score(y_test,y_pred)
cm = confusion_matrix(y_test,y_pred)

print(f"x_test: {x_test}")
print(f"y_test: {y_test}")
print(f"y_pred: {y_pred}")
print(f"accuracy: {acc}")
print(f"confusion matrix: {cm}")

# Soal Ketiga
x = [[1],[2],[3],[4],[5],[6],[7]]
y = [0,0,0,1,1,1,1]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.3, random_state=10
)

model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
acc = accuracy_score(y_test,y_pred)
cm = confusion_matrix(y_test,y_pred)

print(f"y_test: {y_test}")
print(f"y_pred: {y_pred}")
print(f"accuracy: {acc}")
print(f"confusion_matrix: {cm}")

# Soal Keempat
x = [
    [1,50],
    [2,55],
    [3,60],
    [4,65],
    [5,70],
    [6,75],
    [7,80],
    [8,85]
]
y = [0,0,0,0,1,1,1,1]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.25, random_state=5
)
model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
acc = accuracy_score(y_test,y_pred)
cm = confusion_matrix(y_test,y_pred)

pred_baru = model.predict([[6,75]])
print(f"x_test: {x_test}")
print(f"y_test: {y_test}")
print(f"y_pred: {y_pred}")
print(f"accuracy: {acc}")
print(f"confusion matrix: {cm}")
print(f"Pred_baru: {pred_baru}")

# Soal kelima
x = [
    [1,50,60],
    [2,55,65],
    [3,60,70],
    [4,65,75],
    [5,70,80],
    [6,75,85],
    [7,80,90],
    [8,85,95]
]

y = [0,0,0,0,1,1,1,1]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.25, random_state=42
)
model = LogisticRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

acc = accuracy_score(y_test,y_pred)
cm = confusion_matrix(y_test,y_pred)

pred_baru = model.predict([[6,78,88]])
print(f"x_test: {x_test}")
print(f"y_test: {y_test}")
print(f"y_pred: {y_pred}")
print(f"accuracy: {acc}")
print(f"confusion matrix: {cm}")
print(f"Pred_baru: {pred_baru}")