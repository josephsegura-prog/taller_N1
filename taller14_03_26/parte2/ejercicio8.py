
# Ejercicio 8: T(n) = T(n-1) + log n → Θ(n log n)
def sum_logs(n):
    if n <= 1:
        return 0
    import math
    return sum_logs(n-1) + math.log(n)