a, b = map(int, input().split())
for number in range(a, b + 1):
    if number % 2 == 0:
        print(number, end=' ')