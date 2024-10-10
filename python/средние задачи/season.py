def get_season(month, day):
    if (month == 12 and day >= 21) or (month <= 2) or (month == 3 and day < 20):
        return "Зима"
    elif (month == 3 and day >= 20) or (month <= 5) or (month == 6 and day < 21):
        return "Весна"
    elif (month == 6 and day >= 21) or (month <= 8) or (month == 9 and day < 22):
        return "Лето"
    elif (month == 9 and day >= 22) or (month <= 11) or (month == 12 and day < 21):
        return "Осень"
    else:
        return "Неверная дата"

month = int(input("Введите месяц (1-12): "))
day = int(input("Введите день (1-31): "))
season = get_season(month, day)
print(f"Дата {day}/{month} попадает в сезон: {season}")