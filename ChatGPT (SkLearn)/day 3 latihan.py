import os
os.system('cls')

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score


# Soal Pertama
x = [[1],[2],[3],[4],[5]]
y = [10,20,30,40,50]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.2
)

model = LinearRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

print(f"x_test: {x_test}")
print(f"y_test: {y_test}")
print(f"y_pred: {y_pred}")

mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)


print(f"MSE: {mse}")
print(f"R2: {r2}")

# Soal Kedua
x = [[2],[4],[6],[8],[10],[12]]
y = [5,10,15,20,25,30]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.33, random_state=1
)

model = LinearRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print(f"x_test: {x_test}")
print(f"y_test: {y_test}")
print(f"y_pred: {y_pred}")

print(f"mse: {mse}")
print(f"r2: {r2}")

# Soal Ketiga
x = [[1],[2],[3],[4],[5],[6],[7]]
y = [50,55,60,65,70,75,80]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=3, random_state=10
)

model = LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print(f"coef: {model.coef_}")
print(f"intercept: {model.intercept_}")
print(f"y_pred: {y_pred}")

print(f"mse: {mse}")
print(f"r2: {r2}")


# Soal Keempat
x = [[10],[20],[30],[40],[50],[60],[70],[80]]
y = [15,25,35,45,55,65,75,85]

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
print(f"y_pred: {y_pred}")
print(f"MSE: {mse}")
print(f"R2: {r2}")

#soal Kelima

x = [[150],[160],[170],[180],[190],[200],[210],[220]]
y = [50,55,60,65,70,75,80,85]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size = 0.25, random_state=42
)

model = LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

tinggi = model.predict([[175]])

print(f"x_test: {x_test}")
print(f"y_test: {y_test}")

print(f"prediksi model: {y_pred}")

print(f"MSE: {mse}")
print(f"R2: {r2}")

print(f"Prediksi tinggi 175 cm: {tinggi}")