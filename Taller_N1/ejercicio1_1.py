# Ejercicio 1.1 — Operaciones O(1)

# 1. Decidir si n es par o impar
def es_par(n):
    return "Par" if n % 2 == 0 else "Impar"

# 2. Obtener el último dígito de n
def ultimo_digito(n):
    # El módulo 10 devuelve el último dígito
    return n % 10

# 3. Devolver el mayor entre dos números a y b
def mayor(a, b):
    # Comparación directa, siempre constante
    if a > b:
        return a
    else:
        return b

# Ejemplo de uso
n = 57
a, b = 12, 45

print("¿n es par o impar?:", es_par(n))
print("Último dígito de n:", ultimo_digito(n))
print("Mayor entre a y b:", mayor(a, b))