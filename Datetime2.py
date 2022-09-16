from datetime  import datetime
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