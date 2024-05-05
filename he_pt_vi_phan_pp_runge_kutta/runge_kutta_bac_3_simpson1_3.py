import numpy as np
#Thay doi ham nay
def f(y,t):
    return y - t**2 + 1
y0 = 0.5 #y(0)
t0 = 0 #t0
h = 0.25 
n = 2
#Khong sua doan nay
def runge_kutta_bac_3_simpson1_3(y0,t0,h,n):
    y = np.zeros(n+1)
    t = np.zeros(n+1)
    y[0] = y0
    t[0] = t0
    theta = -1
    for i in range(n):
        k1 = h*f(y[i], t[i])
        k2 = h*f(y[i] + k1/2, t[i] + h/2)
        k3 = h*f(y[i] + theta*k1 + (1-theta)*k2, t[i] + h)
        y[i+1] = y[i] + (k1 + 4*k2 + k3)/6
        t[i+1] = t[i] + h
    return y,t
result = runge_kutta_bac_3_simpson1_3(y0 = y0, t0 = t0, h = h, n = n)
print('t: ', end='')
print(result[1])
print('y: ', end='')
print(result[0])
