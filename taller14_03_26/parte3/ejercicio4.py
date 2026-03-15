# Ejercicio 4: Potenciación rápida
def fast_pow(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        half = fast_pow(a, b//2)
        return half * half
    else:
        return a * fast_pow(a, b-1)

