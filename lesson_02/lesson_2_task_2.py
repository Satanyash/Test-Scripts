input_year = 2000


def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


result = is_year_leap(input_year)
print("год", input_year, ":", result)
