import math

def bisection_method(f, a, b, epsilon):
    if f(a) * f(b) >= 0:
        print("Không có nghiệm trong khoảng đã cho!")
        return None

    while abs(b - a) > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return [c, (a + b) / 2]

# Định nghĩa hàm f(x) = e^x - 2
def f(x):
    return math.exp(x) - 2

# Khoảng phân li nghiệm
a = 0
b = 2

# Độ chính xác epsilon
epsilon = 0.01

# Gọi hàm bisection_method để tìm nghiệm
[nghiem_ao, nghiem] = bisection_method(f, a, b, epsilon)

if nghiem is not None:
    print("Nghiệm của phương trình e^x - 2 = 0 là:", nghiem)
    print("Sai số (lấy khoảng cách của 2 kết quả sau nhé):" + str(f(nghiem_ao)) + " và " + str(f(nghiem)))

else:
    print("Không tìm thấy nghiệm trong khoảng đã cho!")  
