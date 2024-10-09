def range_array(n):
    return [i for i in range(1, n + 1)]

n = int(input("Введите размер массива n: "))
arr = range_array(n)

for i in range(len(arr)):
    print(arr[i], end=' ')