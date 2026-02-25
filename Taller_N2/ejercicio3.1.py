
import time




print("\n--- Ejercicio 3.1: Intersección de Listas ---")

# RETO A: Solución ingenua con bucles anidados → O(n²)
def interseccion_ingenua(lista1, lista2):
    """
    Complejidad: O(n * m) ≈ O(n²) si las listas tienen el mismo tamaño.
    Estrategia: para cada elemento de lista1, recorrer lista2 completa.
    """
    resultado = []
    for elem1 in lista1:             # O(n)
        for elem2 in lista2:         # O(m) por cada elem1 → total O(n*m)
            if elem1 == elem2:
                if elem1 not in resultado:
                    resultado.append(elem1)
    return resultado

# RETO B: Solución eficiente con set → O(n)
def interseccion_eficiente(lista1, lista2):
    """
    Complejidad: O(n + m) ≈ O(n).
    Estrategia: convertir lista2 a set para búsqueda en O(1) amortizado.
    Un set usa tabla hash internamente → buscar elem en set es O(1).
    """
    set2 = set(lista2)      # Construir el set: O(m)
    resultado = []
    for elem in lista1:     # O(n) iteraciones
        if elem in set2:    # Búsqueda O(1) — no O(m) como en la lista
            resultado.append(elem)
    return resultado

# Versión pythónica usando operador de sets
def interseccion_pythonica(lista1, lista2):
    """
    Complejidad: O(n + m).
    Versión más compacta usando el operador & de sets.
    """
    return list(set(lista1) & set(lista2))

# ── Documentación: ¿por qué el set es más rápido? ──
# En el Módulo 1 vimos que lim(n→∞) n / n² = 0, lo que significa que O(n)
# es ASINTÓTICAMENTE mejor que O(n²). La versión con set explota esto:
# al construir set2 una sola vez en O(m), cada búsqueda posterior es O(1)
# (gracias al hash), reduciendo el total de O(n*m) a O(n+m) = O(n).
# Para n=10,000: la versión ingenua hace ~100,000,000 operaciones,
# la versión set hace ~20,000 operaciones. ¡5,000 veces más rápida!

# Prueba de corrección
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [3, 4, 5, 6, 7, 8, 9]

print()
print(f"  lista1 = {lista_a}")
print(f"  lista2 = {lista_b}")
print()
print(f"  interseccion_ingenua:    {sorted(interseccion_ingenua(lista_a, lista_b))}")
print(f"  interseccion_eficiente:  {sorted(interseccion_eficiente(lista_a, lista_b))}")
print(f"  interseccion_pythonica:  {sorted(interseccion_pythonica(lista_a, lista_b))}")

# Comparación de tiempos reales
print()
print("  Comparación de tiempos (listas de 3,000 elementos):")
import random
grande1 = list(range(3000))
grande2 = list(range(1500, 4500))
random.shuffle(grande1)
random.shuffle(grande2)

inicio = time.time()
interseccion_ingenua(grande1, grande2)
tiempo_ingenua = time.time() - inicio

inicio = time.time()
interseccion_eficiente(grande1, grande2)
tiempo_eficiente = time.time() - inicio

print(f"  Ingenua  (O n²): {tiempo_ingenua:.4f} segundos")
print(f"  Con set  (O n):  {tiempo_eficiente:.6f} segundos")
if tiempo_ingenua > 0 and tiempo_eficiente > 0:
    print(f"  La versión con set fue {tiempo_ingenua/tiempo_eficiente:.0f}x más rápida ✓")

