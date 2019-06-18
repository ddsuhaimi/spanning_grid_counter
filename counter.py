import numpy as np
import scipy.sparse as scs


def make_matrix(num_of_rows, num_of_cols):
    '''
    this function construct and return the adjacency matrix of a grid graph
    params:
        num_of_rows : how many rows does the grid graph has
        num_of_cols : how many columns does the grid graph
        basically, what is the dimension of the grid graph 

    '''
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
    '''
    this function calculates the number of spanning tree using matrix tree theorem
    params :
        num_of_rows : how many rows does the grid graph has
        num_of_cols : how many columns does the grid graph
        basically, what is the dimension of the grid graph        
    '''
    A = make_matrix(num_of_rows, num_of_cols)

    # calculate any cofactor of its Laplacian graph (see Matrix Tree theorem)
    new_L = scs.csgraph.laplacian(A)[1:, 1:]
    result = int(np.round(np.linalg.det(new_L)))
    return result


print(calc_num_spanning(4, 4))
