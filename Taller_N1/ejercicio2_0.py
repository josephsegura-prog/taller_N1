def busqueda_lineal(lista, objetivo):
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones += 1
        if lista[i] == objetivo:
            return i, comparaciones  # índice y número de comparaciones
    return -1, comparaciones  # no encontrado

lista = list(range(1, 11))  # lista del 1 al 10

# Mejor caso: valor en la primera posición
print("Mejor caso:", busqueda_lineal(lista, 1))  # O(1)

# Caso promedio: valor en la mitad
print("Caso promedio:", busqueda_lineal(lista, 5))  # O(n)

# Peor caso: valor en la última posición
print("Peor caso:", busqueda_lineal(lista, 10))  # O(n)

# Peor caso: valor no está
print("Peor caso (no encontrado):", busqueda_lineal(lista, 11))  # O(n)