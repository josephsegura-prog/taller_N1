# Ejercicio 9: T(n) = T(n-3) + n^3 → Θ(n^4)

def sum_cubes(n):
    if n <= 0:
        return 0
    return sum_cubes(n-3) + n**3
