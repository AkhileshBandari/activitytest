import calendar
year = int (input("year:"))
month = int(input("month:"))
cal = calendar.month(year, month)
print(cal)