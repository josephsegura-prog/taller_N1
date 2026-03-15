
# Ejercicio 6: T(n) = T(n-1) + n → Θ(n^2)
def sum_n(n):
    if n == 0:
        return 0
    return sum_n(n-1) + n

