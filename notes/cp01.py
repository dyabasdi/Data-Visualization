import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# define vector - 1d list of numbers
u = np.array([7, 3, 5])
print(u)

# print the vector length
print('Length of the vector: ', len(u))

# shape of the vector
print('Shape of the vector: ', u.shape)

# define a matrix
A = np.matrix([[4, 9, 2], [3, 5, 7], [8, 1, 6]])
print(A)

# get the dimension of A
print('Shape of A: ', A.shape)
print('Num of rows in A: ', A.shape[0])
print('Num of cols in A: ', A.shape[1])

# define a column vector
v = np.matrix([[2], [5], [8]])
print(v)

# define a row vector
w = np.matrix([[3, 5, 7]])
print(w)

# transpose a vector
x = np.matrix([[9, 5, 1]])
print(x)
print('x transposed: ',x.transpose())

# slicing a matrix
print(A)
print()
print('first column: \n', A[:, 0])
print('second row: \n', A[1,:])
print('top left 2x2: \n', A[0:2, 0:2])
print('bottom right 2x2: \n', A[1:3, 1:3])

# dot product
u = np.array([4, 9, 2])
v = np.array([3, 5, 7])
w = np.dot(u, v)
print('dot product: ', w)

# matrix multiply
A = np.matrix([[4, 9], [3, 5], [8, 1]])
B = np.matrix([[2, 5, 8], [6, 5, 4]])
C = A * B
print(C)

# element by element multiplication
A = np.matrix([[4, 9], [5, 7], [8, 1]])
B = np.matrix([[6, 7], [8, 3], [5, 9]])
C = np.multiply(A, B)
print(C)

# check the version
print(pd.__version__)

# create a Series - a column in a table
a = [3, 6, 4]
a = pd.Series(a)
print(a)

# create your own index or labels
s = pd.Series(a, index =['x', 'y', 'z'])
print(s)

# read a csv
df = pd.read_csv('./files/fit.csv')

# sanity checks
df.shape
print(df.head(5))
print(df.tail(5))
df.info()
df.describe()
pd.options.display.max_rows = 200

print(df)