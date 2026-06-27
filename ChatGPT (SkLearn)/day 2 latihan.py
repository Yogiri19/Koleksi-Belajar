import os
os.system('cls')

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# x = [[1],[2],[3],[4],[5],[6],[7],[8]]
# y = [50,55,65,70,80,85,90,95]

# x_train,x_test,y_train,y_test = train_test_split(
#     x,y,test_size=0.25, random_state=42
# ) 

# model = LinearRegression()

# model.fit(x_train,y_train)
# prediksi = model.predict(x_test)

# print(f"data test: ", x_test)
# print(f"data asli: {y_test}")
# print(f"nilai prediksi: {prediksi}")


# Soal Pertama
print("=====1======")
x = [[1],[2],[3],[4],[5]]
y = [10,20,30,40,50]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(x_train,y_train)

prediksi = model.predict(x_test)

print(f"data test: {x_test}")
print(f"data asli: {y_test}")
print(f"Nilai Prediksi; {prediksi}")


# Soal Kedua
print("=====2======")
x = [[2],[4],[6],[8],[10],[12]]
y = [5,10,15,20,25,30]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.33, random_state=1
)

model = LinearRegression()
model.fit(x,y)

prediksi = model.predict(x_test)
print(f"x_test: {x_test}")
print(f"y_test: {y_test}")
print(f"Prediksi: {prediksi}")

# Soal Ketiga
print("=====3======")
x = [[1],[2],[3],[4],[5],[6],[7]]
y = [50,55,65,70,75,85,90]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.3, random_state=10
)

model = LinearRegression()
model.fit(x_train,y_train)

prediksi = model.predict(x_test)

print(f"data test: {x_test}")
print(f"nilai asli: {y_test}")
print(f"Prediksi model; {prediksi}")

# Soal Keempat
print("=====4======")
x = [[10],[20],[30],[40],[50],[60],[70],[80]]
y = [15,25,35,45,55,65,75,85]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.25, random_state=5
)

model = LinearRegression()
model.fit(x,y)
prediksi = model.predict(x_test)

print(f"coef: {model.coef_}")
print(f"data set: {x_test}")
print(f"nilai asli: {y_test}")
print(f"Prediksi: {prediksi}")

# Soal Kelima
print("=====5======")
x = [[150],[160],[170],[180],[190],[200],[210],[220]]
y = [50,55,60,65,70,75,80,85]
  
  
x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size=0.25, random_state=42
)

model = LinearRegression()
model.fit(x,y)

prediksi = model.predict(x_test)
print(f"data test: {x_test}")
print(f"berat asli: {y_test}")
print(f"Prediksi berat: {prediksi}")