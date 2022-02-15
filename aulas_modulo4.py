

def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 100 == 0:
            if year % 400 != 0:
                return False
            elif year % 400 == 0:
                return True
    else:
        return False


def days_in_month(year, month):
    retorno = is_year_leap(year)
    if retorno:
        if month == 2:
            days = 29
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            days = 31
        elif month == 4 or month == 6 or month == 9 or month == 11:
            days = 30
    else:
        if month == 2:
            days = 28
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            days = 31
        elif month == 4 or month == 6 or month == 9 or month == 11:
            days = 30
    return days


test_years = [1900, 2000, 2016, 1987]
test_months = [1, 3, 7, 11]
test_results = [31, 31, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "--> ", end="")
    results = days_in_month(yr, mo)
    if results == test_results:
        print("OK")
    else:
        print("Failed")









