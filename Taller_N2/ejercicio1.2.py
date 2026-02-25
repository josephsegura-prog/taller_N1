import math

# Ejercicio 1.2 — NIVEL INTERMEDIO
# Demostrar que ln(n) = O(n)

print("\n--- Ejercicio 1.2 ---")
print("f(n) = ln(n),  g(n) = n  →  demostrar que ln(n) = O(n)")
print()
print("Aplicamos L'Hôpital (ambas tienden a ∞):")
print()
print("  lim(n→∞)  ln(n) / n")
print("= lim(n→∞)  (1/n) / 1     ← derivadas")
print("= lim(n→∞)  1/n")
print("= 0")
print()

# Verificación numérica
print("Verificación numérica (el límite se aproxima a 0):")
for n in [10, 100, 1000, 10000, 1000000]:
    L = math.log(n) / n
    print(f"  n = {n:>9} → ln(n)/n = {L:.8f}")

print()
print("Conclusión: L = 0")

