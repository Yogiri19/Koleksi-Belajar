import os
os.system('cls')

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
x = [[1],[2],[3],[4],[5],[6],[7],[8]]
y = [50,55,65,70,80,85,90,95]

x_train,x_test,y_train,y_test = train_test_split(
    x,y, test_size= 0.25, random_state=42
)

model = LinearRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

print("x test: " , x_test)
print("nilai asli: ",y_test)
print("nilai prediksi: ",y_pred)

mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print("MSE: ", mse)
print("R2: ", r2)