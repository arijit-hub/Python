"""
Created by: Arijit Ghosh
Topic: LU Decomposition of a Matrix (with/without Pivoting!)
Part of ANLA Assignment-4
"""

import numpy as np


def lu(A):
    '''Computes the LU Decomposition without pivoting'''
    # TODO
    
    ## Getting the shape of the matrix A ##
    m = A.shape[0]

    ## Initializing the Upper triangular matrix to be A..
    # A at first... ##
    U = A.copy().astype(np.complex128)

    ## Setting the lower triangular matrix L to be ... 
    # identity first ... ##
    L = np.eye(m , dtype = np.complex128)

    for i in range(m-1):
        for j in range(i + 1 , m):

            ## Setting the value of L(i , j) ##
            L[j , i] = U[j , i] / U[i , i] 

            ## row (j) = row(j) - L(j,i) * row(i) ##
            U[j] = U[j] -  L[j , i] * U[i]

    return (L, U)


def maxabs_idx(A):
    '''Returns the row and column index of maximum value of abs(A)'''
    # TODO

    ## np.argmax returns a flattened index ##
    ## unravelling it gives the row and column coordinate ##
    i , j = np.unravel_index(np.argmax(abs(A)) , A.shape)
    return (i, j)


def lu_complete(A):
    '''Returns the LU factorization after Complete Pivoting (Row and Col Swap)'''
    # TODO
    U = A.copy().astype(np.complex128)
    m = A.shape[0]
    L = np.zeros((m , m) , dtype=np.complex128)
    P = np.eye(m , dtype=np.complex128)
    Q = np.eye(m , dtype=np.complex128)

    for i in range(m-1):
        ## getting the smaller subpart of U to grab the max val index ##
        small_U = U[i : , i:].copy()
        max_row , max_col = maxabs_idx(small_U)

        ## Adding i to make the maximum index w.r.t the bigger U ##
        max_row = max_row + i
        max_col = max_col + i

        ## Row swap for P matrix ##
        P[[i , max_row]] = P[[max_row , i]]

        ## Col swap for Q matrix ##
        Q[: , [i , max_col]] = Q[:, [max_col , i]]
        
        ## Swapping row and col for U matrix ##
        U[[i , max_row]] =  U[[max_row , i]]
        U[: , [i , max_col]] = U[:, [max_col , i]]

        ## Swapping row and col for L matrix ##
        L[[i , max_row]] =  L[[max_row , i]]
        L[: , [i , max_col]] = L[:, [max_col , i]]

        for j in range(i + 1 , m):
            L[j , i] = U[j , i] / U[i , i]
            U[j] = U[j] - L[j ,i] * U[i]

    ## Since I initialized L with zeros, to get 1's in diagonal... # 
    # adding with Identity ##
    L = np.eye(m) + L
    return (P, Q, L, U)


## Optional test ##
A = np.random.randn(100 , 100)

L , U = lu(A)
print(f'LU without pivot error {np.max(np.abs(L@U - A))}')

P, Q, L, U = lu_complete(A)
print(f'LU with pivot error {np.max(np.abs(L@U - P@A@Q))}')


