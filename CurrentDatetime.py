# Converting the date time Objects

# YYYY/MM/DD  HH/MM/SS
from datetime import datetime
current = datetime.now()

req_format = datetime.strftime(current, "%Y/%m/%d %H/%M/%S")
print(req_format)

##

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	
##


# Example 1: datetime to string using strftime()

from datetime import datetime

now = datetime.now() # current date and time
print(now)

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time1)

date_time2 = now.strftime("%d/%m/%Y, %H:%M:%S")
print("date and time:",date_time2)
# Example 1: datetime to string using strftime()

from datetime import datetime

now = datetime.now() # current date and time
print(now)

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time1)

date_time2 = now.strftime("%d/%m/%Y, %H:%M:%S")
print("date and time:",date_time2)
