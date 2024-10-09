def deposit(n, k, b):
    monthly_rate = k / 100
    current_balance = b
    for _ in range(n):
        current_balance += current_balance * monthly_rate
        
    return current_balance

n = int(input("Введите количество месяцев (n): "))
k = float(input("Введите процентную ставку (k): "))
b = float(input("Введите начальный баланс (b): "))

result = deposit(n, k, b)
print(f"Баланс через {n} месяцев: {result:.2f} тенге")