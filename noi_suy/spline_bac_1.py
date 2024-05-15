import numpy as np
from scipy.interpolate import interp1d

# Input data points
x = np.array([0,2,5])
y = np.array([1,1,4]) 

# Create linear spline function
linear_spline = interp1d(x, y, kind='linear')

# Print output functions
print("Ham noi suy spline bac 1:")
for i in range(len(x) - 1):
    slope = (linear_spline(x[i+1]) - linear_spline(x[i])) / (x[i+1] - x[i])
    intercept = linear_spline(x[i]) - slope * x[i]
    print(f"f(x) = {slope:.2f} * x + {intercept:.2f}\t\t\t voi {x[i]} <= x <= {x[i+1]}")
