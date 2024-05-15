import numpy as np
def f(x):
    return x**2 - 2*x - 2
epsilon = 0.001
count = 0
x0 = 1
x1 = 2
result = f(x1)
while (abs(result) > epsilon):
    count += 1
    s = (f(x1) - f(x0)) / (x1 - x0)
    x0 = x1
    x1 = x1 - result / s
    result = f(x1)
    
print('x = ', end='')
print(x1)
print('f(x) = ', end='')
print(f(x1))
print('loop count = ', end='')
print(count)
