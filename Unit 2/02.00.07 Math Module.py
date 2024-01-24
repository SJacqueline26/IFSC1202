# We have to use math.ceil because we imported the entire math module
import math
x = 7 /2
print(x)
y = math.ceil(x)
print(y)
# We can use floor because we explicitly imported it from the math module 
from math import floor
x = 7 / 2
print(x)
y = floor(x)
print(y)
print(2.5 ** 3.5)