def f(x):
    return x**2 - x - 2

def g(x):
    return x - (x**2 - x - 2) / (2*x - 1)

def fixed_point_iteration(x0, tolerance=1e-6, max_iterations=100):
    x = x0
    for i in range(max_iterations):
        x_next = g(x)
        if abs(x_next - x) < tolerance:
            return x_next
        x = x_next
    return None

# Tìm nghiệm của phương trình f(x) = 0
x_initial = 2.02
solution = fixed_point_iteration(x_initial)
if solution is not None:
    print("Nghiệm của phương trình là:", solution)
else:
    print("Không tìm thấy nghiệm trong số lần lặp cho trước.")

# Tìm điểm bất động của hàm g(x)
fixed_point = fixed_point_iteration(x_initial, tolerance=1e-6, max_iterations=1000)
if fixed_point is not None:
    print("Điểm bất động là:", fixed_point)
else:
    print("Không tìm thấy điểm bất động trong số lần lặp cho trước.")
