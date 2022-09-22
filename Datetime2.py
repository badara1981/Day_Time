from datetime  import datetime, timedelta
from xmlrpc.client import _datetime_type

now = datetime.now()
year = now.strftime("%Y")
print("Year:",year)

month = now.strftime("%m")
print("month:",month)

day = now.strftime("%d")

time  = now.strftime("%H: %M: %S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y ,%H:%M:%S" )
print("date and time:", date_time)

# Task 2
import  datetime

date_time_str = 'Jan 25 2022 7:40AM'
date_time_obj = datetime.datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')

print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)

import datetime 
todayDate = datetime.date.today()
if (todayDate - todayDate.replace(day=1)).days > 25:
    x= todayDate + datetime.timedelta(30)
    x.replace(day=1)
    print (x)
else:
    print (todayDate.replace(day=1))

    #Manipulation  Addition and Substraction
    #Substraction
from datetime import datetime
s1 = '10:04:00'
s2 = '11:03:11' # for example
format = '%H:%M:%S'
time = datetime.strptime(s2, format) - datetime.strptime(s1, format)
print (time)

##Adding hours  or minutes or Second to datetime
#from datetime import datetime, timedelta

## Adding hours or minutes or seconds to datetime
from datetime import datetime, timedelta
 
## Original datetime
datetime_original = datetime(year=2022, month=9, day=19)
print("\nOriginal date: ", datetime_original, "\n")
 
## Adding Hours
hours_to_add = 12
datetime_new = datetime_original + timedelta(hours = hours_to_add)
print("After adding hours: ", datetime_new, "\n")
 
## Adding Minutes
minutes_to_add = 45
datetime_new = datetime_new + timedelta(minutes = minutes_to_add)
print("After adding minutes: ", datetime_new, "\n")
 
## Adding Seconds
seconds_to_add = 33
datetime_new = datetime_new + timedelta(seconds = seconds_to_add)
print("After adding seconds: ", datetime_new, "\n")
 
## Adding Microseconds
microseconds_to_add = 12345
datetime_new = datetime_new + timedelta(microseconds = microseconds_to_add)
print("After adding microseconds: ", datetime_new, "\n")

### Current date in different formats

from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)

#EXER 2
#  Current time using datetime object
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	