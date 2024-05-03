import numpy as np

#y' = f(y,z,t)
def f(y,z,t):
    return z
#z' = g(y,z,t)
def g(y,z,t):
    return -2*z - 2*y + np.sin(t) + np.cos(t)
y0 = 0.5 #y(0)
t0 = 0 #t0
h = 0.25 
n = 2
#Khong sua doan nay
def euler(y0,z0,t0,h,n):
    y = np.zeros(n+1)
    z = np.zeros(n+1)
    t = np.zeros(n+1)
    y[0] = y0
    z[0] = z0
    t[0] = t0
    for i in range(n):
        y[i+1] = y[i] + h*f(y[i],z[i],t[i])
        z[i+1] = z[i] + h*g(y[i],z[i],t[i])
        t[i+1] = t[i] + h
    return y,z,t
result = euler(y0 = y0, t0 = t0, h = h, n = n)
print('t: ', end='')
print(result[2])
print('y: ', end='')
print(result[0])
print('z: ', end='')
print(result[1])
