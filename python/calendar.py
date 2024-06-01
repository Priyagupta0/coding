import calendar
year=int(input("Enter year:"))
month=int(input("Enter month:"))
print(calendar.month(year,month))

print()

from datetime import datetime
now=datetime.now()
dt_string=now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time = ",dt_string)