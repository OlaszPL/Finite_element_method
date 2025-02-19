import numpy as np
from scipy import integrate

# predefined functions and constants

def eps_r(x):
    if 0 <= x <= 1: return -1
    elif 1 < x <= 2: return 5

    return 1

rho = 2

# calculate functions

def e(i, x, h):
    if x < (i - 1) * h or x > (i + 1) * h:
        return 0
    elif x < i * h:
        return (x - (i - 1) * h) / h
    
    return ((i + 1) * h - x) / h

def e_prim(i, x, h):
    if x < (i - 1) * h or x > (i + 1) * h:
        return 0
    elif x < i * h:
        return 1 / h
    
    return -1 / h

# vectorized functions to be used with integrate.fixed_quad
eps_r_vec = np.vectorize(eps_r)
e_vec = np.vectorize(e, excluded=['i', 'h'])
e_prim_vec = np.vectorize(e_prim, excluded=['i', 'h'])


def b(i, j, h):
    left = max(0, (i - 1) * h, (j - 1) * h) # not to integrate over 0
    right = min((i + 1) * h, (j + 1) * h, 3)

    return -e(i, 0, h) * e(j, 0, h)\
        - integrate.fixed_quad(lambda x: e_prim_vec(i, x, h) * e_prim_vec(j, x, h), left, right)[0]\
            if abs(i - j) <= 1 else 0 

def l(j, h):
    left = max(0, (j - 1) * h)
    right = min((j + 1) * h, 3)
    
    return -2 * e(j, 0, h) - integrate.fixed_quad(lambda x: (rho / eps_r_vec(x)) * e_vec(j, x, h), left, right)[0]

# prepare matrices

def calculate_A(n, h):
    matrix = np.empty((n, n))

    for i in range(n):
        for j in range(n):
            matrix[i][j] = b(j, i, h)

    return matrix

def calculate_B(n, h):
    matrix = np.empty(n)

    for i in range(n):
        matrix[i] = l(i, h)

    return matrix


# calculate equation solution

def solve(n):
    h = 3 / n

    A = calculate_A(n, h)
    B = calculate_B(n, h)

    x = [i * h for i in range(n + 1)] # we've got n + 1 points
    # we can use alphas as w, because of the (alpha_i * e_i) characteristics
    y = np.append(np.linalg.solve(A, B), 0) - 5 # we've got 0 at 3 from Dirichlet condition, 5 subtracted because of the shift

    return np.column_stack((x, y))