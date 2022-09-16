from datetime  import datetime

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