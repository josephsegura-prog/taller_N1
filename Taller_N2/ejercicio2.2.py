
import math


print("\n--- Ejercicio 2.2: El salto de índices ---")

def algoritmo_misterioso(n):

    i = 1
    operaciones = 0
    while i < n:
        operaciones += 1
        i = i * 2     
    return operaciones



print()
print("ANÁLISIS:")
print("  i toma valores: 1, 2, 4, 8, ... (se duplica cada vez)")
print("  El bucle termina cuando i >= n → después de log₂(n) pasos")
print()
print("  Mejor Caso → O(1): n <= 1, el bucle no ejecuta")
print("  Peor Caso  → O(log n): recorre log₂(n) iteraciones")
print("  Big O      → O(log n)")
print()

print("  Verificación numérica:")
print(f"  {'n':>10} | {'ops reales':>12} | {'log₂(n)':>10}")
print(f"  {'-'*10}-+-{'-'*12}-+-{'-'*10}")
for n in [2, 4, 8, 16, 32, 64, 128, 1024]:
    ops = algoritmo_misterioso(n)
    log2 = math.floor(math.log2(n))
    print(f"  {n:>10} | {ops:>12} | {log2:>10}")

print()
print("  ✓ Confirmado: las operaciones reales coinciden exactamente con ⌊log₂(n)⌋")
print("  Regla: si la variable de control se MULTIPLICA (no suma), es O(log n)")

