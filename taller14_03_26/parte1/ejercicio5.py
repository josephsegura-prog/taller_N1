# Ejercicio 5: T(n) = 7T(n/4) + n^2
# Solución: Θ(n^2)
# Ejemplo: Algoritmo de Karatsuba para multiplicación de enteros grandes
def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    high1, low1 = divmod(x, 10**m)
    high2, low2 = divmod(y, 10**m)
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1+high1), (low2+high2))
    z2 = karatsuba(high1, high2)
    return (z2*10**(2*m)) + ((z1-z2-z0)*10**m) + z0
