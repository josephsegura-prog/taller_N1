import time


def fibonacci_recursivo(n):

    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

print()
print("  Árbol de llamadas para fib(5):")
print("             fib(5)")
print("            /      \\")
print("         fib(4)   fib(3)")
print("        /    \\   /    \\")
print("     fib(3) fib(2) fib(2) fib(1)")
print("     /  \\")
print("  fib(2) fib(1)")
print()


contador = [0]

def fibonacci_contado(n):
    contador[0] += 1
    if n <= 1:
        return n
    return fibonacci_contado(n - 1) + fibonacci_contado(n - 2)

print(f"  {'n':>4} | {'Resultado':>12} | {'Llamadas reales':>16} | {'2^n':>10}")
print(f"  {'-'*4}-+-{'-'*12}-+-{'-'*16}-+-{'-'*10}")
for n in [5, 10, 15, 20, 25, 30]:
    contador[0] = 0
    resultado = fibonacci_contado(n)
    llamadas = contador[0]
    potencia = 2**n
    print(f"  {n:>4} | {resultado:>12} | {llamadas:>16} | {potencia:>10}")

print()
print("  Respuesta a la pregunta técnica (n=50):")
print("  ─────────────────────────────────────────────────────")
print(f"  2^50 ≈ {2**50:,} llamadas")
print("  A 1,000,000,000 operaciones/segundo → ~13 DÍAS")
print("  Además se agotaría la pila de llamadas (RecursionError)")
print("  ∴ La computadora se 'bloquea' porque nunca terminaría")
print("    en tiempo razonable.")
print()

# ── Solución eficiente con memoización: O(n) ──
print("  Solución eficiente — Memoización O(n):")
print("  (Cada valor se calcula UNA sola vez y se guarda en el diccionario)")

def fibonacci_memo(n, memo={}):
    """
    Memoización: almacena resultados ya calculados.
    Complejidad: O(n) — cada F(k) se calcula exactamente una vez.
    """
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print()
for n in [10, 30, 50, 100]:
    inicio = time.time()
    resultado = fibonacci_memo(n)
    tiempo = time.time() - inicio
    print(f"  fib_memo({n:>3}) = {resultado:>25}  ({tiempo:.6f}s) ← instantáneo")

print()
print("  ✓ Con memoización, fib(50) se calcula en microsegundos")
print("    vs. días con la versión recursiva simple.")
