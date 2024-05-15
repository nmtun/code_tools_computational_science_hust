#imports
import numpy as np
from scipy.interpolate import CubicSpline
x = np.array([0,2,5])
y = np.array([1,1,4]) 
# apply natural cubic spline interpolation
cs = CubicSpline(x, y,bc_type='natural')
# Print the polynomial functions
rounding = 4
for i in range(len(cs.c[0])):
    cubic_coeff = round(cs.c[0, i], rounding)
    quadratic_coeff = round(cs.c[1, i], rounding)
    linear_coeff = round(cs.c[2, i], rounding)
    constant = round(cs.c[3, i], rounding)
    original_x = round(cs.x[i], rounding)
    
    polynomial = f"{cubic_coeff}*(x - {original_x})^3 + {quadratic_coeff}*(x - {original_x})^2 + {linear_coeff}*(x - {original_x}) + {constant}"
    print(f"{x[i]} <= x <= {x[i+1]}:\t {polynomial}")