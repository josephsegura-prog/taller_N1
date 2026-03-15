

# Ejercicio 2: T(n) = 4T(n/2) + n^2
# Solución: Θ(n^2 log n)
# Ejemplo: Multiplicación de matrices clásica (divide en 4 submatrices)
def matrix_mult(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
