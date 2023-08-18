import datetime

year = int(input('year of birth : '))
Month = int(input('month of birth : '))
Day = int(input('day of birth : '))

date = datetime.datetime.now()

year_2 = date.year - year
day_year = year_2 * 365
month_2 = date.month - Month
day_month = month_2 * 30
day2 = date.day - Day

days = day_year + day_month + day2
week = days // 7
Second = days * 86400

print('you have weeks :',week)
print('you have days :',days)
print('you have seconds :',Second)