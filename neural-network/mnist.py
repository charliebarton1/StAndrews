from keras.datasets import mnist
from matplotlib import pyplot as plt
# (train_X, train_y), (test_X, test_y) = mnist.load_data()
# Print shapes
# print('X_train: ', int(test_X.shape[0]))

##print(train_X[0].shape)
##train_X_flat = train_X.reshape(60000, 784)    
##print(train_X_flat[0])

import numpy as np

X = np.array([[1, 10], [2, 20], [3, 30], [4, 40]])
y = np.array([0, 1, 0, 1])

perm = np.random.permutation(len(X))
X_shuffled = X[perm]
y_shuffled = y[perm]

print(X_shuffled)
print(y_shuffled)