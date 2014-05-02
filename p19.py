#! python
import sys
import math
import euler

def num_days_in_year(year):
    num = 365
    if year % 4 == 0 and not(year % 100 == 0 and year % 400 != 0):
        num = 366
    return num

def first_of_month_to_day_of_year(month, year):
    days_in_year = num_days_in_year(year)
    day = 0

    #if month >= 1:  # January
    if month >= 2:  # February
        day += 31
    if month >= 3:  # March
        day += 28
        if days_in_year == 366:
            day += 1
    if month >= 4:  # April
        day += 31
    if month >= 5:  # May
        day += 30
    if month >= 6:  # June
        day += 31
    if month >= 7:  # July
        day += 30
    if month >= 8:  # August
        day += 31
    if month >= 9:  # September
        day += 31
    if month >= 10: # October
        day += 30
    if month >= 11: # November
        day += 31
    if month >= 12: # December
        day += 30

    return day

def days_since_jan_1900(month, year):
    days = sum([num_days_in_year(y) for y in range(1900, year)])
    days += first_of_month_to_day_of_year(month, year)
    return days

def day_of_week(month, year):
    return days_since_jan_1900(month, year) % 7

def day_str(day):
    if day == 0:
        return 'Monday'
    if day == 1:
        return 'Tuesday'
    if day == 2:
        return 'Wednesday'
    if day == 3:
        return 'Thursday'
    if day == 4:
        return 'Friday'
    if day == 5:
        return 'Saturday'
    if day == 6:
        return 'Sunday'

def main():
    num_sundays = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if day_of_week(month, year) == 6:
                num_sundays += 1

    print(num_sundays)

if __name__ == "__main__":
    main()
