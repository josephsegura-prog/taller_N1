def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    comparaciones = 0  # contador de comparaciones

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        comparaciones += 1  # cada vez que comparamos

        if lista[medio] == objetivo:
            return medio, comparaciones  # encontrado
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1, comparaciones  # no encontrado

# Lista ordenada
lista = list(range(1, 101))  # del 1 al 100

# Mejor caso: elemento en el centro
print(busqueda_binaria(lista, 50))  # debería dar índice 49 y pocas comparaciones

# Peor caso: elemento no está
print(busqueda_binaria(lista, 101))  # debería dar -1 y más comparaciones

# Peor caso: elemento en un extremo
print(busqueda_binaria(lista, 1))  # índice 0 y varias comparaciones

for n in [100, 1000, 10000]:
    lista = list(range(1, n+1))
    _, comps = busqueda_binaria(lista, n+1)  # peor caso: no está
    print(f"n={n}, comparaciones={comps}")