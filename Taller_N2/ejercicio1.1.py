import math
import time


print("MÓDULO 1: CRITERIO DEL LÍMITE")
print("=" * 60)


print("\n--- Ejercicio 1.1 ---")
print("f(n) = 7n² + 5n + 2  →  demostrar que es O(n²)")
print()
print("Aplicamos el límite con g(n) = n²:")
print()
print("  lim(n→∞)  (7n² + 5n + 2) / n²")
print("= lim(n→∞)  7 + 5/n + 2/n²")
print("= 7 + 0 + 0")
print("= 7")
print()

# Verificación numérica
print("Verificación numérica (el límite se aproxima a 7):")
for n in [10, 100, 1000, 10000, 100000]:
    f_n = 7*n**2 + 5*n + 2
    g_n = n**2
    L = f_n / g_n
    print(f"  n = {n:>7} → L = {L:.6f}")

print()
print("Conclusión: L = 7 (constante finita ≠ 0)")
print("∴ f(n) = Θ(n²)  ⊆  O(n²)  ✓")

