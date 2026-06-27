import os
os.system('cls')

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

x = [
    [1,60,50],
    [2,65,60],
    [3,70,65],
    [4,75,70],
    [5,80,80],
    [6,85,85],
    [7,90,90],
    [8,95,95]
]

y = [55,60,70,75,85,90,95,98]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.25, random_state=42
)
model = LinearRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

print(f"x_test: {x_test}")
print(f"y_test: {y_test}")
print(f"y_pred: {y_pred}")

print(f"Coef: {model.coef_}")
print(f"Intercept: {model.intercept_}")

mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print(f"mse: {mse}")
print(f"r2: {r2}")

prediksi_baru = model.predict([[6,85,80]])
print(f"prediksi nilai mahasiswa baru: {prediksi_baru}")