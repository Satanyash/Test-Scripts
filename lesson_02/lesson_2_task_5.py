def month_to_season(month):
    if month >= 1 and month <= 2 or month == 12:
        return ("Зима")
    if month >= 3 and month <= 5:
        return ("Весна")
    if month >= 6 and month <= 8:
        return ("Лето")
    if month >= 9 and month <= 11:
        return ("Осень")


month = 2
print(month_to_season(month))
