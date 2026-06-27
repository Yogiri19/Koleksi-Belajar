import tensorflow as tf

print("TensorFlow Version :", tf.__version__)

# MEMBUAT TENSOR

tensor = tf.constant([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nTensor Awal")
print(tensor)

# SHAPE

print("\nShape Awal :", tensor.shape)

# RESHAPE

reshape_1 = tf.reshape(tensor, (3, 2))

print("\nReshape (3,2)")
print(reshape_1)

reshape_2 = tf.reshape(tensor, (6,))

print("\nReshape (6,)")
print(reshape_2)

# INDEXING

print("\nIndexing")

print("Baris Pertama :")
print(tensor[0])

print("\nBaris Kedua :")
print(tensor[1])

print("\nElemen [0][1] :")
print(tensor[0][1].numpy())

# SLICING

print("\nSlicing")

print("Kolom Pertama")
print(tensor[:, 0])

print("\nKolom Kedua")
print(tensor[:, 1])

print("\n2 Kolom Pertama")
print(tensor[:, :2])

# CONCATENATE

a = tf.constant([
    [1, 2],
    [3, 4]
])

b = tf.constant([
    [5, 6],
    [7, 8]
])

gabung_baris = tf.concat([a, b], axis=0)

print("\nConcat Axis 0")
print(gabung_baris)
gabung_kolom = tf.concat([a, b], axis=1)
print("\nConcat Axis 1")
print(gabung_kolom)

# STACK
stack = tf.stack([a, b])
print("\nStack")
print(stack)

print("Shape Stack :", stack.shape)

# EXPAND DIMS
vector = tf.constant([10, 20, 30, 40])
print("\nVector")
print(vector)

expand = tf.expand_dims(vector, axis=0)
print("\nExpand Axis 0")
print(expand)

print("Shape :", expand.shape)
expand2 = tf.expand_dims(vector, axis=1)
print("\nExpand Axis 1")
print(expand2)
print("Shape :", expand2.shape)

# SQUEEZE
tensor_baru = tf.constant([
    [[1],
     [2],
     [3]]
])

print("\nTensor Sebelum Squeeze")
print(tensor_baru)
print("Shape :", tensor_baru.shape)

squeeze = tf.squeeze(tensor_baru)
print("\nTensor Setelah Squeeze")
print(squeeze)

print("Shape :", squeeze.shape)

# FOR LOOP
print("\nFor Loop")
for baris in tensor:
    print(baris.numpy())

# WHILE LOOP
i = tf.Variable(0)
print("\nWhile Loop")
while i.numpy() < tensor.shape[0]:
    print(tensor[i.numpy()].numpy())
    i.assign_add(1)

# IF ELSE
jumlah_elemen = tf.size(tensor)
if jumlah_elemen.numpy() > 5:
    print("\nTensor Besar")
else:
    print("\nTensor Kecil")

# LATIHAN
data = tf.constant([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("\nData")
print(data)
print("\nShape")
print(data.shape)
print("\nBaris Pertama")
print(data[0])
print("\nKolom Kedua")
print(data[:, 1])

ubah = tf.reshape(data, (1, 9))
print("\nReshape")
print(ubah)



# Soal Pertama
import tensorflow as tf

tensor = tf.constant([
    [1,2],
    [3,4],
    [5,6]
])
print(f"Tensor: \n{tensor}\n")
print(f"Shape tensor: \n{tensor.shape}\n")
reshape1 = tf.reshape(tensor,(2,3))
print(f"reshape1: \n{reshape1}\n")
print(f"Shape reshape1: \n{reshape1.shape}\n")

# Soal Kedua
import tensorflow as tf
tensor = tf.constant([
    [10, 20, 30],
    [40, 50, 60]
])
print(f"baris pertama: \n{tensor[0]}\n")
print(f"baris Kedua: \n{tensor[1]}\n")
print(f"element: \n{tensor[1][2]}\n")

# Soal Ketiga
tensor = tf.constant([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f"Kolom Pertama: \n{tensor[:,0]}\n")
print(f"Kolom ketiga: \n{tensor[:,2]}\n")
print(f"dua kolom pertama: \n{tensor[:,:2]}")

# Soal Keempat
import tensorflow as tf
a = tf.constant([
    [1, 2],
    [3, 4]
])
b = tf.constant([
    [5, 6],
    [7, 8]
])
gabung_baris = tf.concat([a,b], axis=0)
print(f"concat axis 0 \n{gabung_baris}\n")

gabung_kolom = tf.concat([a,b], axis=1)
print(f"concat axis 1 \n{gabung_kolom}\n")

stack = tf.stack([a,b])
print(f"stack: \n{stack}\n")
print(f"Shape Stack: \n{stack.shape}\n")

# Soal Kelima
import tensorflow as tf
data = tf.constant([
    [10, 20, 30],
    [40, 50, 60]
])
print(f"Shape data: \n{data.shape}\n")
ukuran = tf.size(data)
print(f"Size: \n{ukuran}\n")
print(f"Kolom kedua: \n{data[:, 1]}\n")
data_reshape = tf.reshape(data, [3,2])
print(f"data reshape: \n{data_reshape}\n")

expand_dims = tf.expand_dims(data, axis=0)
print(f"Expand: \n{expand_dims}\n")

shape = tf.shape(expand_dims)
print(f"shape: \n{shape}\n")

tensor = tf.constant([
    [[1],
     [2],
     [3]]
])
squ = tf.squeeze(tensor)
print(f"Squeeze: \n{squ}\n")
print(f"Shape tensor: \n{squ.shape}\n")