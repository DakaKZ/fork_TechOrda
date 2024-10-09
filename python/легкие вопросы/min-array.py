def min_value(array):
    if len(array) == 0:
        return 0
    
    minimum = array[0]
    
    for num in array:
        if num < minimum:
            minimum = num
            
    return minimum

array = list(map(int, input("Введите элементы массива через пробел: ").split()))
result = min_value(array)
print(f"Минимальное число в массиве: {result}")
