
#função ano bissexto
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

#função dias no mês
def days_in_month(yr, mo):
    bissexto = is_year_leap(yr)
    if bissexto and mo == 2:
        days = 29
    else:
        if mo == 2:
            days = 28
        elif mo == 1 or mo == 3 or mo == 5 or mo == 7 or mo == 8 or mo == 10 or mo == 12:
            days = 31
        elif mo == 4 or mo == 6 or mo == 9 or mo == 11:
            days = 30
    return days


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "--> ", end="")
    results = days_in_month(yr, mo)
    if results == test_results[i]:
        print("OK")
    else:
        print("Failed")









