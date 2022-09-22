
##String to datetime

# datetime object containing current date and time

from datetime import datetime

datetime_str = '09/22/22 13:55:26'

datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

print(type(datetime_object))
print(datetime_object)  # printed in default format

## String to date object

date_str = "09-22-2022"
date_object = datetime.strptime(date_str, '%m-%d-%Y').date()

print(type(date_object))
print(date_object)

#String to time object
#We can use time() function alongwith strptime() function to convert string to time object.

time_str = '15::55::26'
time_object = datetime.strptime(time_str, '%H::%M::%S').time()
print(type(time_object))
print(time_object)
##

import time

time_obj = time.strptime(time_str, '%H::%M::%S')
print(type(time_obj))
print(time_obj)

# default formatting - "%a %b %d %H:%M:%S %Y"
print(time.strptime('Wed Sep 19 14:55:02 2018'))


#Python time strptime() example
#Let’s see some examples of using time module strptime() function.