def is_perfect_number(num):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

def find_perfect_numbers_in_range(start, end):
    perfect_numbers = []
    for number in range(start, end + 1):
        if is_perfect_number(number):
            perfect_numbers.append(number)
    return perfect_numbers

start_range = 0
end_range = 1000

perfect_numbers = find_perfect_numbers_in_range(start_range, end_range)

print(f"Совершенные числа в диапазоне от {start_range} до {end_range}: {perfect_numbers}")