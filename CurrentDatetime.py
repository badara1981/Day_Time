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

  #Note: In the above example, we have imported the datetime class from the datetime module. Then, we used now method to get a datetime object containing current date and time.

#Using datetime.strftime() method, we then created a string representing current time.

# If you need to create a time object containing current time, you can do something like this.

#  datetime to string using strftime()

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


#  1: datetime to string using strftime()

from datetime import datetime

now = datetime.now() # current date and time
print(now)

year = now.strftime("%Y")
print("year:", year)
from datetime import datetime

now = datetime.now() # current date and time
print(now)

year = now.strftime("%Y")# current Year
print("year:", year)

month = now.strftime("%m") # current month
print("month:", month)

day = now.strftime("%d") #  Current day 
print("day:", day)

time = now.strftime("%H:%M:%S") # current time
print("time:", time)

date_time1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time1)

date_time2 = now.strftime("%d/%m/%Y, %H:%M:%S")
print("date and time:",date_time2)

# 
# Example 2: Creating string from a timestamp

from datetime import datetime

timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)

print("Date time object:", date_time)

d = date_time.strftime("%m/%d/%Y, %H:%M:%S")
print("Output 2:", d)	

d = date_time.strftime("%d %b, %Y")
print("Output 3:", d)

d = date_time.strftime("%d %B, %Y")
print("Output 4:", d)

d = date_time.strftime("%I%p")
print("Output 5:", d)
