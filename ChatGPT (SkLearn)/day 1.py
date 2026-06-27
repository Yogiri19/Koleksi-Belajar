import os
os.system('cls')

from sklearn.linear_model import LinearRegression

# data input (jam belajar)
x = [[1], [2], [3], [4], [5]] # ini adalah matrix
 
# data output (nilai)
y = [50, 55, 65, 70, 80]

# Membuat model
model = LinearRegression()

# melatih model dengan data
model.fit(x,y)

# melihat parameter model
print("coef:", model.coef_)
print("intercept:", model.intercept_)

# prediksi nilai jika belajar 6 jam
prediksi = model.predict([[6]])

print("prediksi nilai: ", prediksi)
