
print("\n--- Ejercicio 2.1: El buscador de pares ---")

def buscar_par_especifico(lista, objetivo):
    pasos = 0
    for i in range(len(lista)):
        pasos += 1
        if lista[i] % 2 == 0 and lista[i] == objetivo:
            return True, pasos
    return False, pasos



print()
print("ANÁLISIS:")
print("  Mejor Caso → O(1): el objetivo es par y está en la posición 0")
print("  Peor Caso  → O(n): el objetivo no existe, se recorre todo")
print("  Big O      → O(n) (búsqueda lineal)")
print()

lista = [1, 3, 5, 7, 2, 9, 11]  # el 2 está en posición 4

encontrado, pasos = buscar_par_especifico(lista, 2)
print(f"  Buscar 2 en {lista}")
print(f"  Encontrado: {encontrado}, Pasos: {pasos} (no es el primer elemento)")

lista_mejor = [4, 1, 3, 5, 7]   # el 4 es par y está primero
encontrado, pasos = buscar_par_especifico(lista_mejor, 4)
print(f"\n  Buscar 4 en {lista_mejor}")
print(f"  Encontrado: {encontrado}, Pasos: {pasos} ← Mejor caso O(1)")

lista_peor = [1, 3, 5, 7, 9]    # ningún par existe
encontrado, pasos = buscar_par_especifico(lista_peor, 4)
print(f"\n  Buscar 4 en {lista_peor}")
print(f"  Encontrado: {encontrado}, Pasos: {pasos} ← Peor caso O(n)")
