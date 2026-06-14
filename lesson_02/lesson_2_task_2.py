def is_year_leap(year):
    return year % 4 == 0


current_year = 2024
result = is_year_leap(current_year)
input(f"год {current_year}:{result}")
