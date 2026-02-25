import math


print("\n--- Ejercicio 1.3 ---")
print("f(n) = n!  vs  g(n) = 2ⁿ  →  ¿cuál crece más rápido?")
print()
print("Analizamos n! / 2ⁿ:")
print()
print("  n! / 2ⁿ = (1/2)·(2/2)·(3/2)·(4/2)·...·(n/2)")
print("  Para n > 2, cada factor k/2 > 1 → el producto diverge a ∞")
print()

# Verificación numérica
print("Verificación numérica (el cociente crece sin límite):")
for n in [1, 5, 10, 15, 20]:
    factorial = math.factorial(n)
    potencia = 2**n
    cociente = factorial / potencia
    print(f"  n = {n:>2} → {n}! = {factorial:>12} | 2^{n} = {potencia:>7} | n!/2ⁿ = {cociente:.2f}")

print()
print("Conclusión: lim(n→∞) n!/2ⁿ = ∞")
print("∴ 2ⁿ = O(n!)  →  n! crece MUCHO más rápido que 2ⁿ  ✓")
print()
print("Jerarquía de crecimiento (menor a mayor):")
print("O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)")

