#11. Implementación y diseño de algoritmos.
#Escribe una función (puedes usar python o pseudocódigo estructurado) que reciba como parámetros un arreglo de números enteros y el tamaño de dicho arreglo. Tu objetivo es que la función cumpla con dos requisitos:
#1. Debe imprimir en pantalla todas las combinaciones posibles de pares de números del arreglo (por ejemplo, si el arreglo es [1, 2], debe imprimir 1-1, 1-2, 2-1, 2-2).
#2. El algoritmo debe tener una complejidad temporal asintótica exacta de O(n^2) en el peor de los casos.
#Escribe tu código en el recuadro inferior y, al lado, explica brevemente en un par de líneas por qué la estructura que diseñaste garantiza una complejidad de O(n^2).

def imprimir_pares(arr, n):
    for i in range(n):
        for j in range(n):
            print(f"{arr[i]} - {arr[j]}")

# Ejemplo de uso:
mi_arreglo = [1, 2, 3]
tamaño = len(mi_arreglo)
imprimir_pares(mi_arreglo, tamaño)