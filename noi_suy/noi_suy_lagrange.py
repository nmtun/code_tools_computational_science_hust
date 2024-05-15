from scipy.interpolate import lagrange
x = [0, 1, 2, 3]
y = [0, 0.8415, 0.9093, 0.1411]
result = lagrange(x, y)
print("ham noi suy lagrange: ")
print(result)