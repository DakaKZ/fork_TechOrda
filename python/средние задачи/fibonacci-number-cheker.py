def is_fibonacci(num):
    if num < 0:
        return False

    a, b = 0, 1
    while a < num:
        a, b = b, a + b

    return a == num

number = 25

if is_fibonacci(number):
    print(f"Число {number} является числом Фибоначчи.")
else:
    print(f"Число {number} не является числом Фибоначчи.")