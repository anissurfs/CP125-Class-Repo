# Lab 01 Exercise 6: Leap Year Detector
def is_leap_year (year):
    div4 = year % 4
    div100 = year % 100
    div400 = year % 400
    if div4 == 0 and div100 != 0:
        return True
    elif div100 == 0 and div400 == 0:
        return True
    else:
        return False