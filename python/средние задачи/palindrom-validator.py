user_input = input("Введите строку: ")

cleaned_input = user_input.replace(" ", "").lower()

if cleaned_input == cleaned_input[::-1]:
    print("Введенная строка является палиндромом.")
else:
    print("Введенная строка не является палиндромом.")