def is_perfect_number(num):
    if num < 1:
        return False

    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    
    return divisors_sum == num

number = int(input("Введите число для проверки: "))

if is_perfect_number(number):
    print(f"Число {number} является совершенным числом.")
else:
    print(f"Число {number} не является совершенным числом.")