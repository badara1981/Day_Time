# Converting the date time Objects

# YYYY/MM/DD  HH/MM/SS
from datetime import datetime
current = datetime.now()

req_format = datetime.strftime(current, "%Y/%m/%d %H/%M/%S")
print(req_format)