import os
os.system('cls')

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


x = [[1],[2],[3],[4],[5],[6],[7],[8]]
y = [50,55,65,70,80,85,90,95]

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.25, random_state=42
) 

model = LinearRegression()

model.fit(x_train,y_train) # Menggunakan data training
prediksi = model.predict(x_test) # karena x_test sudah berbentuk list/array

print(f"data test: ", {x_test})
print(f"data asli: {y_test}")
print(f"nilai prediksi: {prediksi}")