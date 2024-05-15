import math

def f(x):
    return x**3 - 3*(x**2) - 5

def f_prime(f, x):
    h = 0.0001  # Độ dịch chuyển nhỏ
    return (f(x + h) - f(x - h)) / (2 * h)

def newton_method(f, x0, epsilon):
    x = x0
    while abs(f(x)) > epsilon:
        x = x - f(x) / f_prime(f, x)
    return x

x0 = 3.5  # Giá trị khởi tạo x0
epsilon = 0.0001  # Độ chính xác mong muốn

solution = newton_method(f, x0, epsilon)
print("Nghiệm của phương trình là:", solution)
