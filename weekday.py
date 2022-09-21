
##
from calendar import week, weekday
import datetime

intDay = datetime.date(year=2020, month=12, day=2).weekday()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days[intDay])

##
import datetime

week_num = datetime.date(2022,9,21).weekday()
week_days = [ "Monday", "Tuesday", "Wednesday","Thursday", "Friday" , "Saturday" "Sunday" ]
print(week_days[week_num])

##
import datetime
print(datetime.date(2022,9,21).strftime("%A"))# FULL NAME FOR EXAMPLE Wednesday

print(datetime.date(2022,9,21).strftime("%a"))## incomplete  sentence for example WED

print(datetime.date(2022,9,21).strftime("%Y"))

print(datetime.date(2022,9,21).strftime("%y"))

print(datetime.date(2022,9,21).strftime("%M"))

print(datetime.date(2022,9,21).strftime("%S"))


## YOU can also use CALENDER 
import calendar

week_num = calendar.weekday(2022,9, 21)
week_days = [ "Monday", "Tuesday", "Wednesday","Thursday", "Friday" , "Saturday" "Sunday" ]
print(week_days[week_num])