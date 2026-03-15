
# Ejercicio 7: T(n) = T(n-2) + n^2 → Θ(n^3)
# Ejemplo: cálculo acumulativo
def sum_squares(n):
    if n <= 0:
        return 0
    return sum_squares(n-2) + n**2
