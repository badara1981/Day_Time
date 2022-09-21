from datetime import datetime
my_date_string = "Mar 11 2011 11:31AM"

datetime_object = datetime.strptime(my_date_string, '%b %d %Y %I:%M%p' )

print(type(datetime_object))
print(datetime_object)

#%b is for Month as locale’s abbreviated name. Like Jan, Feb, …, Dec

#%B is for Month as locale’s full name. Like January, February, …, December

##

