import numpy as np
import scipy.sparse as scs

def make_matrix(num_of_rows, num_of_cols):
    n = num_of_rows*num_of_cols
    M = np.zeros((n, n))
    for r in range(0, num_of_rows):
        for c in range(0, num_of_cols):
            i = r*num_of_cols + c
            if c > 0:
                M[i-1, i] = M[i, i-1] = 1
            if r > 0:
                M[i-num_of_cols, i] = M[i, i-num_of_cols] = 1
    return M

def calc_num_spanning(num_of_rows, num_of_cols):
    A = make_matrix(num_of_rows, num_of_cols)
    new_L = scs.csgraph.laplacian(A)[1:, 1:]
    result = int(np.round(np.linalg.det(new_L)))
    return result

print(calc_num_spanning(4,4))