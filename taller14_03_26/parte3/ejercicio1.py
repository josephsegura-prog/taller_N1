
# Ejercicio 1: Suma de un arreglo
def suma_arreglo(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    mid = len(arr)//2
    return suma_arreglo(arr[:mid]) + suma_arreglo(arr[mid:])
