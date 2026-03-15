
# Ejercicio 10: T(n) = T(n-2) + n log n → Θ(n^2 log n)

def sum_nlogn(n):
    if n <= 0:
        return 0
    import math
    return sum_nlogn(n-2) + n*math.log(n)

