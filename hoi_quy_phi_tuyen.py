import numpy as np
from numpy.linalg import inv
#Nhap bo du lieu
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([10,12,15,13,19,22])
#Nhap bac cua da thuc hoi quy (degree = 2 la hoi quy bac 2)
degree = 5
matrixA = np.zeros((degree + 1, degree + 1))
matrixB = np.zeros((degree + 1, 1))

for i in range(degree + 1):
    for j in range(degree + 1):
        if matrixA[i][j] == 0:
            matrixA[i][j] = np.sum(x ** (i + j))
        if i != j:
            matrixA[j][i] = np.sum(x ** (i + j))
    matrixB[i] = np.sum(y * (x ** i))

result = np.dot(inv(matrixA), matrixB)
for i in range(len(result)):
    print(f'a_{i} = {result[i, 0]:.5f}')

for i in range(len(result)):
    print(f'{result[i, 0]:.5f}*x^{i}', end=' ')
    if i != len(result) - 1:
        print("+", end=' ')