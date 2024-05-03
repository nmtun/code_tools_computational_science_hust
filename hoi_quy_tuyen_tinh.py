import numpy as np
from numpy.linalg import inv
#Nhap bo du lieu
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([10,12,15,13,19,22])


const_sum = 0
x_sum = 0
x2_sum = 0
y_sum = 0
xy_sum = 0

for i in range(len(x)):
    const_sum += 1
    x_sum += x[i]
    x2_sum += (x[i] ** 2)
    y_sum += y[i]
    xy_sum += (x[i] * y[i])

matrixA = np.array([[const_sum, x_sum ], 
                    [x_sum    , x2_sum]])
matrixB = np.array([y_sum    , xy_sum])
result = np.dot(inv(matrixA), matrixB)
b = result[0]
m = result[1]

max_loss = 0
avg_loss = 0
root_mean_square_error = 0
Lmb = 0

for i in range(len(x)):
    yhat = m * x[i] + b
    diff = abs(y[i] - yhat)
    avg_loss += diff
    root_mean_square_error += diff ** 2
    max_loss = max(max_loss, diff)
    Lmb += (y[i] - yhat) ** 2

avg_loss /= len(x)
root_mean_square_error = np.sqrt(root_mean_square_error / len(x))

    
print(f"m = {m:.2f}")
print(f"b = {b:.2f}")
print(f"Ham hoi quy: y(x) = {m:.2f} * x + {b:.2f}")
print(f"Sai so trung binh h E_1(f) = {avg_loss:.2f}")
print(f"Can bac 2 tong cac binh phuong sai so: E_2(f) = {root_mean_square_error:.2f}")
print(f"Sai so cuc dai E_inf(f) = {max_loss:.2f}")
print(f"Tieu chi binh phuong toi thieu: L(m, b) = {Lmb:.2f}")