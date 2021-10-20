# This is code I wrote for my Python Certification course.

def is_year_leap(year):
#
# Your code from LAB 4.3.1.6.
#
    if (year % 100 == 0) and (year % 400 == 0):
        return True
    elif (year % 100 == 0) and (year % 400 != 0):
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
#
# Your code from LAB 4.3.1.7.
#
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    else:
        return None

def day_of_year(year, month, day):
#
# Write your new code here.
#
    my_total = 0
    for i in range(1, month):
        my_total += days_in_month(year, i)
    my_total += day
       
    return my_total

print(day_of_year(2000, 12, 31))