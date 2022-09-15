import re

given_string = "5+1"
print(re.match("\\d+\\s?[\\+\\*/%-]\\s?\\d+", given_string))

#

def make_happy(txt):
    return re.sub("(?<=[:8x;])\(",')',txt)

given_string = "print:[('x(')"

print(make_happy(given_string))


# time
import time



