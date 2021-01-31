"""
Write a function is_orthogonal(mx) that given a square matrix (list of lists where each list represents a row), determines if the matrix is orthogonal, returning the appropriate boolean value. A matrix M is orthogonal if MMᵀ = I (i.e. the product of M by its transpose is equal to the identity matrix). The identity matrix is a square matrix in which all the elements of the principal diagonal are ones and all other elements are zeros.

    for the matrix mx=[[-1, 0], [0,1]], the output should be True
    for the matrix [[-2,3], [4,-1]], the output should be False

"""

def is_orthogonal(mx):
    transp = mx.copy()
    transp[0][1] = mx[1][0]
    transp[1][0] = mx[0][1]
    M_rows = len(mx)
    M_cols = len(mx[0])
    T_rows = len(transp)
    T_cols = len(transp[0])
    if M_cols != T_rows:
        return []
    else:
        result = []
        for row in range(M_rows):
            lista = []
            for col in range(T_cols):
                lista += [0]
            result += [lista]
        for i in range(M_rows):
            for j in range(T_cols):
                for k in range(M_cols):
                    result[i][j] += mx[i][k] * transp[k][j]
        return result == [[1, 0], [0 ,1]]
