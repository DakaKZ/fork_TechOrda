def is_valid_date(date_str):
    day, month, year = map(int, date_str.split('.'))
    
    if year < 1:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
            
    return True

user_input = input("Введите дату в формате DD.MM.YYYY: ")

if is_valid_date(user_input):
    print(f"Дата {user_input} является корректной.")
else:
    print(f"Дата {user_input} не является корректной.")