
# Ejercicio 2: Máximo y mínimo
def max_min(arr):
    if len(arr) == 1:
        return arr[0], arr[0]
    mid = len(arr)//2
    left_max, left_min = max_min(arr[:mid])
    right_max, right_min = max_min(arr[mid:])
    return max(left_max, right_max), min(left_min, right_min)
