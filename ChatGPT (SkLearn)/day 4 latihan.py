import os
os.system('cls')

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Soal Pertama
x = [
    [1,60],
    [2,65],
    [3,70],
    [4,75],
    [5,80]
]

y = [55,60,65,70,75]

x_train,x_test,y_train,y_test = train_test_split(
x,y, test_size=0.2
)

model = LinearRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
mse = mean_squared_error(y_test,y_train)
r2 = r2_score(y_test,y_pred)

print(f"x_test: {x_test}")
print(f"y_test: {y_test}")
print(f"y_pred: {y_pred}")

print(f"MSE: {mse}")
print(f"R2: {r2}")

# Soal Kedua
x = [
    [1,50,60],
    [2,55,65],
    [3,60,70],
    [4,65,75],
    [5,70,80],
    [6,75,85]
]
y = [55,60,65,70,75,80]
x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.33, random_state=1
)

model = LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

r2 = r2_score(y_test,y_pred)
mse = mean_squared_error(y_test,y_pred)

# Soal Ketiga
x = [
    [2,60,50],
    [3,65,55],
    [4,70,60],
    [5,75,65],
    [6,80,70],
    [7,85,75],
    [8,90,80]
]
y = [55,60,65,70,75,80,85]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.3, random_state=10
)

model = LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

r2 = r2_score(y_test,y_pred)
mse = mean_squared_error(y_test,y_pred)

print(f"intercept: {model.intercept_}")
print(f"y_pred: {y_pred}")
print(f"MSE: {mse}")
print(f"R2: {r2}")


# Soal Keempat
x = [
    [1,60,50],
    [2,65,55],
    [3,70,60],
    [4,75,65],
    [5,80,70],
    [6,85,75],
    [7,90,80],
    [8,95,85]
]

y = [55,60,65,70,75,80,85,90]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.25, random_state=5
)
model = LinearRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print(f"coef: {model.coef_}")
print(f"intercept: {model.intercept_}")
print(f"x_test: {x_test}")
print(f"y_test: {y_test}")
print(f"MSE: {mse}")
print(f"R2: {r2}")


# soal Kelima
x = [
    [1,60,55],
    [2,65,60],
    [3,70,65],
    [4,75,70],
    [5,80,75],
    [6,85,80],
    [7,90,85],
    [8,95,90]
]
y = [55,60,65,70,75,80,85,90]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.25, random_state=42
)
model = LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

mhs_baru = model.predict([[6,88,82]])
print(f"x_test: {x_test}")
print(f"y_test: {y_test}")

print(f"y_pred: {y_pred}")

print(f"MSE: {mse}")
print(f"R2: {r2}")

print(f"Prediksi mhs baru: {mhs_baru}")
