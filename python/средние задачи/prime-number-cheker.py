def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

user_input = int(input("Введите число: "))

if is_prime(user_input):
    print(f"Число {user_input} является простым.")
else:
    print(f"Число {user_input} не является простым.")