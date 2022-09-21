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
