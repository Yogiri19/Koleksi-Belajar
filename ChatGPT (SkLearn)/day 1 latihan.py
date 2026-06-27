import os
os.system("cls")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# x = [10, 20, 30, 40, 50]
# y = [1, 2, 3, 4, 5]
# x_train, x_test, y_train, y_test = train_test_split(
#     x,y, test_size=0.2, random_state=42 # test_size = 0.2
# )
# np.random.seed(42)
# print(x_train)
# print(x_test)
# print(y_train)
# print(y_test)

# model = LinearRegression()
# model.fit(x_train, y_train)
# y_pred = model.predict(x_test)
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# print(f"MSE: {mse}")
# print(f"R2 Score: {r2}")

# x = [10, 20, 30, 40, 50] # 5
# y = [1, 2, 3, 4, 5]

# x_train, x_test, y_train, y_test = train_test_split(
#     x,y, test_size=0.2, random_state=42
# )

# print("x_train: ", x_train)
# print("x_test: ", x_test)
# print("y_train: ", y_train)
# print("y_test: ", y_test)

# df = pd.DataFrame({
#     "umur" : [17,18,19,20,21],
#     "nilai" : [70,75,80,85,90]
# })

# x = df["umur"]
# y = df["nilai"]

# x_train, x_test, y_train, y_test = train_test_split(
#     x,y, test_size=0.4 , random_state=1
# )
# print(x_train)
# print(x_test)

# from sklearn.model_selection import train_test_split

# data = list(range(7))

# train, test = train_test_split(
#     data,
#     test_size=0.3,
#     random_state=1
# )

# print("jumlah train: ", len(train))
# print("Jumlah Test: ", len(test))

# x = np.array([[1],
#               [2],
#               [3],
#               [4],
#               [5]])
# y = np.array([50, 55, 65, 70, 80])

# # Membuat model  
# model = LinearRegression()

# # Melatih model
# model.fit(x,y)
 
# # Prediksi
# prediksi = model.predict([[6]])
# print("Prediksi nilai: ", prediksi)
# print(model.coef_)
# print(model.intercept_)



# # Soal pertama
# x = [[1], [2], [3], [4], [5]]
# y = [3, 5, 7, 9, 11]

# x_train, x_test, y_train, y_test = train_test_split(
#     x,y, test_size=0.2, random_state=42
# )
# print(x_train)
# print(x_test)

# # Soal Kedua
# x = [[2],
#      [4],
#      [6],
#      [8],
#      [10]]

# y = [4, 8, 12, 16, 20]

# model = LinearRegression()
# model.fit(x,y)

# print(model.coef_)
# print(model.intercept_)

# # Soal Ketiga 
# x = [[1],
#      [2],
#      [3],
#      [4]]
# y = [2, 4, 6, 8]

# model = LinearRegression()
# model.fit(x,y)

# prediksi = model.predict([[5]])
# print(prediksi)

# # Soal Keempat
# x = [[1], [2], [3], [4], [5], [6]]
# y = [5, 7, 9, 11, 13, 15]

# x_train, x_test, y_train, y_test = train_test_split(
#     x,y, test_size=0.3 
# )
# print(x_test)

# # Soal Kelima
# jam_belajar = [[1],
#                [2],
#                [3],
#                [4],
#                [5]]
# nilai = [50, 55, 65, 70, 80]

# model = LinearRegression()
# model.fit(jam_belajar, nilai)

# prediksi_nilai = model.predict([[6]])
# print(prediksi_nilai)


# # Soal Keenam
# x = [[10], [20], [30], [40], [50]]
# y = [15, 25, 35, 45, 55]

# x_train, x_test, y_train, y_test = train_test_split(
#     x,y
# )

# model = LinearRegression()
# model.fit(x_train, y_train)

# y_pred = model.predict(x_test)
# mse = mean_squared_error(y_test, y_pred)
# print(mse)

# # # Soal Ketujuh
# x = [[1],[2],[3],[5],[7],[9]]
# y = [2, 6, 10, 14, 18]

# x_train, x_test, y_train, y_test = train_test_split(
#     x,y
# )

# model = LinearRegression()
# model.fit(x_train, y_train)
# y_pred = model.predict(x_test)

# r2 = r2_score(y_test, y_pred)
# print(r2)   

# # Saol Kedelapan
# umur = [18, 19, 20, 21, 22]
# jam_belajar = [2, 3, 4, 5, 6]

# nilai = [60, 65, 70, 75, 80]

# x = [[umur, jam_belajar]]

# model = LinearRegression()
# model.fit(nilai, x)
# print(model.coef_)

# # Soal Pertama
# x = [[1], [2], [3], [4]]
# y = [2, 4, 6, 8]

# model = LinearRegression()
# model.fit(x,y)

# print(f"Coef: ",model.coef_ )
# print(f"Intercapt: ", model.intercept_)

# prediksi = model.predict([[5]])
# print(f"Prediksi: ", prediksi)

# # Soal Kedua
# x = [[1], [2], [3], [4], [5]]
# y = [3, 6, 9, 12, 15]

# model = LinearRegression()
# model.fit(x,y)

# print(f"Coef: ", model.coef_)
# print(f"Intercept: ", model.intercept_)

# # Soal Ketiga
# x = [[2],[4],[6],[8]]
# y = [20,40,60,80]

# model = LinearRegression()
# model.fit(x,y)

# prediksi = model.predict([[10], [12]])
# print(f"Prediksi: {prediksi}")

# # Soal Keempat
# x = [[1],[2],[3],[4],[5],[6]]
# y = [40,50,55,65,70,75]

# model = LinearRegression()
# model.fit(x,y)

# print(f"Coef: {model.coef_}")
# print(f"Prediksi: {model.predict([[ 7]])}")

# # Soal kelima
# x = [[1],[3],[5],[7],[9]]
# y = [10,30,50,70,90]

# model = LinearRegression()
# model.fit(x,y)

# prediksi = model.predict([[2],[4],[6],[8]])
# print(f"Prediksi: {prediksi}")


#==========================================
# # Soal Pertama
# x = [[1],[2],[3],[4],[5]]
# y = [2,4,6,8,10]

# x_train,x_test,y_train,y_test = train_test_split(
#     x,y,random_state=42, test_size=0.2
# )
# print(x_train)
# print(x_test)
# print(y_train)
# print(y_test)

# #Soal Kedua
# x = np.array([10,20,30,40,50,60]).reshape(-1,1)
# y = np.array([1,2,3,4,5,6])

# x_train,x_test,y_train,y_test = train_test_split(
#     x,y,test_size=0.33, random_state=1
# )
# print(x_train)
# print(x_test)

# # Soal Ketiga
# x = np.array([[150,5], [160,6],[170,7],[180,8],[190,9],[200,10]])
# y = np.array([50,55,60,65,70,75])

# x_train,x_test,y_train,y_test = train_test_split(
#     x,y,test_size=0.3, random_state=0
# )

# print(x_train.shape)
# print(x_test.shape)

# # Soal Keempat
# data = {
#     'age' : [21,22,23,24,25,26,27,28],
#     'salary': [3000,3200,3400,3600,3800,4000,4200,4400],
#     'buy': [0,0,0,1,1,1,1,1]
# }

# df = pd.DataFrame(data)
# x = df[['age','salary']]
# y = df[['buy']]

# x_train,x_test,y_train,y_test = train_test_split(
#     x,y,test_size=0.25, random_state=42
# )
# print(  x_train)
# print(x_test)

# # Soal Kelima
# from sklearn.datasets import load_iris
# iris = load_iris()
# x = iris.data
# y = iris.target

# x_train,x_test,y_train,y_test = train_test_split(
#     x,y, test_size=0.2, random_state=42, stratify=y
# )
# model = LinearRegression()
# total = model.fit(x,y)
# print("Total data: ", model)
# print("Train: ",x_train)
# print("Test: ",x_test)