
# Ejercicio 6: Multiplicación de matrices con Strassen
def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0]*B[0][0]]]
    mid = n//2
    # Dividir matrices
    def split(matrix):
        return ( [row[:mid] for row in matrix[:mid]],
                [row[mid:] for row in matrix[:mid]],
                [row[:mid] for row in matrix[mid:]],
                [row[mid:] for row in matrix[mid:]] )
    A11, A12, A21, A22 = split(A)
    B11, B12, B21, B22 = split(B)
    # Operaciones de Strassen
    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, sub(B12, B22))
    M4 = strassen(A22, sub(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(sub(A21, A11), add(B11, B12))
    M7 = strassen(sub(A12, A22), add(B21, B22))
    # Combinar resultados
    C11 = add(sub(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(sub(add(M1, M3), M2), M6)
    # Unir cuadrantes
    new_matrix = []
    for i in range(mid):
        new_matrix.append(C11[i] + C12[i])
    for i in range(mid):
        new_matrix.append(C21[i] + C22[i])
    return new_matrix

def add(A, B):
    return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]

def sub(A, B):
    return [[A[i][j]-B[i][j] for j in range(len(A))] for i in range(len(A))]
