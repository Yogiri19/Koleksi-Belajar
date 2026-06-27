import tensorflow as tf
print(f"Versi: \n{tf.__version__}") # ²³

x = tf.Variable(3.0)

with tf.GradientTape() as tape: # y = 3² = 9
    y = x ** 2

grad = tape.gradient(y, x)
print(f"y: \n{y.numpy()}")
print(f"dy/dx: ", grad.numpy())

# y = x³ + 2x + 1
x = tf.Variable(2.0)

with tf.GradientTape() as tape:
    y = x ** 3 + 2 * x + 1

grad = tape.gradient(y,x) #dy/dx = 3(2²)+2
                          #= 12+2

print(f"y: \n{y}")
print(f"dy/dx: \n{grad.numpy()}")

x = tf.Variable(2.0)
y = tf.Variable(3.0)

with tf.GradientTape() as tape:
    z = x ** 2 + y ** 2

grad = tape.gradient(z, [x,y])
print(f"dz/dx: \n{grad[0].numpy()}")
print(f"dz/dy: \n{grad[1].numpy()}")

x = tf.Variable([1.0, 2.0, 3.0])
with tf.GradientTape() as tape:
    y = x ** 2

grad = tape.gradient(y, x)
print(grad.numpy())

x = tf.Variable([1.0, 2.0, 3.0])
with tf.GradientTape() as tape:
    y = tf.reduce_sum(x ** 2)

grad = tape.gradient(y, x)
print(f"grad: \n{grad.numpy()}")

x = tf.Variable(3.0)
with tf.GradientTape(
    persistent=True
) as tape:
    
    y = x ** 2
    z = x ** 3
dy = tape.gradient(y, x)
dz = tape.gradient(z,x)
print(f"dy/dx: \n{dy.numpy()}")
print(f"dz/dx: \n{dz.numpy()}")

berat = tf.Variable(10.0)
print(f"Awal: \n{berat.numpy()}")

berat.assign(20.0)
print(f"Baru: {berat.numpy()}")

# x mendekati 5
# Loss = (x - 5)²
x = tf.Variable(0.0)
learning_rate = 0.1
for i in range(20):
    with tf.GradientTape() as tape:
        loss = (x - 5) ** 2
    grad = tape.gradient(loss,x)

    x.assign_sub(
        learning_rate * grad
    )
    print(
        f"Epoch {i+1}",
        "x =", x.numpy(),
        "loss =", loss.numpy()
    )

x = tf.Variable(0.0)
lr = 0.1

@tf.function
def train_step():
    with tf.GradientTape() as tape:
        loss = (x - 5) ** 2

    grad = tape.gradient(loss,x)

    x.assign_sub(
        lr * grad
    )
    return loss

for epoch in range(20):
    loss = train_step()

    print(
        epoch + 1,
        x.numpy(),
        loss.numpy()
    )
    
x = tf.Variable([
    [1.0, 2.0],
    [3.0, 4.0]
])
with tf.GradientTape() as tape:
    y = tf.reduce_sum(x ** 2)
grad = tape.gradient(y, x)
print(grad.numpy())

# cari nilai minimum dari
# f(x) = x² + 4x + 4
x = tf.Variable(10.0)
lr = 0.1

for epoch in range(50):
    with tf.GradientTape() as tape:
        loss = x ** 2 + 4 * x + 4

    grad = tape.gradient(
        loss,
        x
    )
    x.assign_sub(
        lr * grad
    )
print(f"x: \n{x.numpy()}")
print(f"f(x): \n{loss.numpy()}")
