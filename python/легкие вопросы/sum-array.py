def sum_array(array):
    total = 0
    
    for num in array:
        total += num
        
    return total

array = [1, 2, 3]
sum_number = sum_array(array)

print(sum_number)