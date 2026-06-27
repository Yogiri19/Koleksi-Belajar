import tensorflow as tf

print(f"Versi: \n{tf.__version__}")

# y=2x+1
x_train = tf.constant(
    [[1.0],
    [2.0],
    [3.0],
    [4.0]]
)
y_train = tf.constant([
    [3.0],
    [5.0],
    [7.0],
    [9.0]
])
print(f"x_train: \n{x_train}")
print(f"y_train: \n{y_train}")

w = tf.Variable(
    tf.random.normal((1, 1))
)

b = tf.Variable(
    tf.random.normal((1,))
)

print(f"weight: \n{w.numpy()}")
print(f"Bias: \n{b.numpy()}")

# y=xw+b
prediksi = tf.matmul(
    x_train,
    w
) + b

print(f"Prediksi: \n{prediksi.numpy()}")

# Loss = 1/n ∑(y_true- y_pred)²
prediksi = tf.matmul(
    x_train,
    w
) + b
loss = tf.reduce_mean(
    (y_train - prediksi) ** 2
)
print(f"loss: \n{loss.numpy()}")

with tf.GradientTape() as tape:
    prediksi = (
        tf.matmul(
            x_train,
            w    
        ) + b
    )
    loss = tf.reduce_mean(
        (y_train - prediksi) ** 2
    )
grad_w, grad_b = tape.gradient(
    loss,
    [w,b]
)
print(f"Gradient W: \n{grad_w.numpy()}")
print(f"Gradient B: \n{grad_b.numpy()}")

learning_rate = 0.01
w.assign_sub(
    learning_rate * grad_w
)
b.assign_sub(
    learning_rate * grad_b
)
print(f"w: \n{w.numpy()}")
print(f"b: \n{b.numpy()}")

learning_rate = 0.01
with tf.GradientTape() as tape:
    prediksi = (
        tf.matmul(
            x_train,
            w
        ) + b
    )
    loss = tf.reduce_mean(
        (y_train - prediksi) ** 2
    )
grad_w, grad_b = tape.gradient(
    loss,
    [w,b]
)
w.assign_sub(
    learning_rate * grad_w
)
b.assign_sub(
    learning_rate * grad_b
)
print(f"loss: \n{loss.numpy()}")

w = tf.Variable(
    tf.random.normal((1,1))
)
b = tf.Variable(
    tf.random.normal((1,))
)
learning_rate = 0.01
for epoch in range(500):
    with tf.GradientTape() as tape:
        prediksi = (
            tf.matmul(
                x_train,
                w
            ) + b
        )
        loss = tf.reduce_mean(
            (y_train - prediksi) ** 2
        )
    grad_w, grad_b = tape.gradient(
        loss,
        [w,b]
    )
    w.assign_sub(
        learning_rate * grad_w
    )
    b.assign_sub(
        learning_rate * grad_b
    )
    if epoch % 50 == 0:
        print(
            f"Epoch {epoch}",
            f"Loss {loss.numpy():.4f}"
        )

print(f"weight: \n{w.numpy()}")
print(f"Bias: \n{b.numpy()}")

x_baru = tf.constant([[10.0]])
prediksi = (
    tf.matmul(
        x_baru,
        w
    ) + b
)
print(f"prediksi: \n{prediksi.numpy()}")

@tf.function
def predict(x):
    return(
        tf.matmul(
            x,
            w
        ) + b
    )
hasil = predict(
    tf.constant([[20.0]])
)
print(f"Hasil: \n{hasil.numpy()}")

x_train = tf.constant([
    [1.0, 2.0],
    [2.0, 3.0],
    [3.0, 4.0],
    [4.0, 5.0]
])
y_train = tf.constant([
    [8.0],
    [13.0],
    [18.0],
    [23.0]
])
print(f"x_train: \n{x_train}")
print(f"y_train: \n{y_train}")

w = tf.Variable(
    tf.random.normal(
        (2,1)
    )
)
b = tf.Variable(
    tf.zeros((1,))
)
print(f"w: \n{w.numpy()}")
print(f"b: \n{b.numpy()}")

learning_rate = 0.01
for epoch in range(500):
    with tf.GradientTape() as tape:
        prediksi = (
            tf.matmul(
                x_train,
                w
            ) + b
        )
        loss = tf.reduce_mean(
             (y_train - prediksi) ** 2
        )
    grad_w, grad_b = tape.gradient(
        loss,
        [w,b]
    )
    w.assign_sub(
        learning_rate * grad_w
    )
    b.assign_sub(
        learning_rate * grad_b
    )
print(f"Loss: \n{loss}")
