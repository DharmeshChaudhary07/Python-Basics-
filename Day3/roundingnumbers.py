################################# Rounding numbers ################################

import math
print(2 - 10)
print(abs(2-5))

print(round(2-5))
print(round(3234.42423432))
print(round(3234.62423432))
print(round(3234.62423432, 2))  # returns the number upto to 2 decimal points

price = 3123.4231
distance = 213.723

print(math.floor(price))
print(math.floor(distance))

print(math.ceil(price))    
print(math.ceil(distance))

print(math.trunc(price))    ## cut down the decimal point regarless of how big it is / without rounding it up
print(math.trunc(distance))