def month_to_season(month):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Ошибка: введите число от 1 до 12"
    
    
print(month_to_season(2))   # Вывод: Зима
print(month_to_season(5))   # Вывод: Весна
print(month_to_season(8))   # Вывод: Лето
print(month_to_season(11))  # Вывод: Осень
print(month_to_season(15))  # Вывод: Ошибка: введите число от 1 до 12