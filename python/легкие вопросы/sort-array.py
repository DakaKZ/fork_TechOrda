def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

array = [7, 5, 9, 1, 4]
bubble_sort(array)

for i in range(len(array)):
    print(array[i], end=" ")