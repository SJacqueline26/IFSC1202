# A variable is created the moment you first assign a value to it.
x = 5
y = "John"
print(x)
print(y)

# Variables do not need to be declared with any particular type and 
# can even change type after they have been set.

x = 4       # x is of type integer
print(x)
x = "Sally" # x is now of type string
print(x)

# String variables can be declared either by 
# using single or double quotes:

x = "John"
print(x)
# is the same as
x = 'John'
print(x)

# Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# And you can assign the same value to multiple variables in one line:

x = y = z = "Orange"
print(x)
print(y)
print(z)
