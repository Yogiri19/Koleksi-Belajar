import os
os.system('cls')
    # LinearRegression
# LinearRegression -> y = ax + b
# bebas dan tanpa batas
# Gampang Overfitting kalo datanya kompleks

    # Ridge
# "Jangan terlalu ekstrim dalam mementukan bobot"
# Ini LinearRegresion + "rem" biar gak kebalasan
# Mengurangi overfitting

    # Lasso
# Kalo fitur gak penting, buang aja
# Mirip Ridge
# otomatis feature selection

    # ElasticNet
# ambil kelebihan Ridge dan Lasso
# bisa seleksi fitur + tetap setabil

from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet

# Contoh Penggunaan
model1 = LinearRegression()
model2 = Ridge(alpha=1.0)
model3 = Lasso(alpha=0.1)
model4 = ElasticNet(alpha=0.1, l1_ratio=0.5)

# training
model1.fit(x_train,y_train)

# prediksi
y_pred = model1.predict(x_test)
