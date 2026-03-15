# Ejercicio 7: Búsqueda en matriz ordenada
def search_matrix(matrix, target):
    n = len(matrix)
    row, col = 0, n-1
    while row < n and col >= 0:
        if matrix[row][col] == target:
            return (row, col)
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    return None
