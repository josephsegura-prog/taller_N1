# ============================================
# Taller Teorema Maestro y Divide y Vencerás
# Lenguaje: Python
# ============================================

# ---- Ejercicios prácticos ----

def suma_lista(lista):
    if len(lista) == 0:
        return 0
    if len(lista) == 1:
        return lista[0]
    mitad = len(lista) // 2
    return suma_lista(lista[:mitad]) + suma_lista(lista[mitad:])

def maximo_minimo(lista):
    if len(lista) == 1:
        return lista[0], lista[0]
    mitad = len(lista) // 2
    max_izq, min_izq = maximo_minimo(lista[:mitad])
    max_der, min_der = maximo_minimo(lista[mitad:])
    return max(max_izq, max_der), min(min_izq, min_der)

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    alto1, bajo1 = divmod(x, 10**m)
    alto2, bajo2 = divmod(y, 10**m)
    z0 = karatsuba(bajo1, bajo2)
    z1 = karatsuba(bajo1 + alto1, bajo2 + alto2)
    z2 = karatsuba(alto1, alto2)
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

def potencia_rapida(base, exponente):
    if exponente == 0:
        return 1
    if exponente % 2 == 0:
        mitad = potencia_rapida(base, exponente // 2)
        return mitad * mitad
    else:
        return base * potencia_rapida(base, exponente - 1)

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    mitad = len(lista) // 2
    izquierda = merge_sort(lista[:mitad])
    derecha = merge_sort(lista[mitad:])
    return combinar(izquierda, derecha)

def combinar(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# ---- Menú interactivo ----
def menu():
    print("\n=== Taller Divide y Vencerás ===")
    print("1. Suma de una lista")
    print("2. Máximo y mínimo")
    print("3. Multiplicación de enteros grandes (Karatsuba)")
    print("4. Potenciación rápida")
    print("5. Ordenación con Merge Sort")
    print("0. Salir")

    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        lista = [1, 2, 3, 4, 5]
        print("Suma:", suma_lista(lista))
    elif opcion == 2:
        lista = [7, 2, 9, 4, 1]
        print("Máximo y mínimo:", maximo_minimo(lista))
    elif opcion == 3:
        print("Karatsuba:", karatsuba(1234, 5678))
    elif opcion == 4:
        print("Potenciación rápida:", potencia_rapida(2, 10))
    elif opcion == 5:
        lista = [5, 3, 8, 1, 2]
        print("Merge Sort:", merge_sort(lista))
    elif opcion == 0:
        print("Adiós!")
        return False
    else:
        print("Opción inválida")
    return True

# ---- Programa principal ----
if __name__ == "__main__":
    seguir = True
    while seguir:
        seguir = menu()