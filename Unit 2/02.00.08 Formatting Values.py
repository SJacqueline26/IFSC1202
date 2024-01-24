from math import pi
# String Examples
print("{}".format("hello"))            #|h|e|l|l|o|
print("{:8s}".format("hello"))         #|h|e|l|l|o| | | |
print("{:>8s}".format("hello"))        #| | | |h|e|l|l|o|
print("{:^8s}".format("hello"))        #| |h|e|l|l|o| | |
print("{:^4.2s}".format("hello"))       #| |h|e| |
# Integer Examples
print("{:4d}".format(42))              #| | |4|2|
print("{:04d}".format(42))             #|0|0|4|2|
# Floating Point Examples
print("{:6.2f}".format(pi))            #| | |3|.|1|4|
print("{:06.2f}".format(pi))           #|0|0|3|.|1|4|
print("{:,.2f}".format(123456789.017)) #|1|2|3|,|4|5|6|,|7|8|9|.|0|2|
# Other Examples

one = "one"
two = "two"
three = "three"

print("{}{}{}".format("one","two","three"))
print("one = {:s}, two = {:s}, three = {:s}".format(one, two, three))
print("one = {:8s}, two = {:8s}, three = {:8s}".format(one, two, three))
print("one = {:.2s}, two = {:.2s}, three = {:.2s}".format(one, two, three))
print("x{:4.1f}x".format(pi))
print('{:,.2f}'.format(123456789.017))

Hi = 8.5
Lo = -4.4

print("{}{}".format(Hi, Lo))
print("Todays high is {}, the low is {}.".format(Hi, Lo))
print("Todays high is {:8.2f}, the low is {:8.2f}.".format(Hi, Lo))

print("{:^8s}{:^8s}".format("Hi","Low"))
print("{:8.1f}{:8.1f}".format(91.5, 66.4))
print("{:8.1f}{:8.1f}".format(101.5, 55.4))
print("{:8.1f}{:8.1f}".format(8.5, -4.4))
