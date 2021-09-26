# About variables (rules):
# Variable names are case sensitive (name and NAME are different variables.
# Must start with a letter or an underscore.
# Can have numbers but can not start with one.


"""
Different types of variables and their rules.
"""
"""
x = 1                   # int
y = 2.5                 # float
name = 'Ranjeet Kumar'  # string
is_cool = True          # Boolean
"""

"""
Multiple assignment
"""
x, y, name, is_cool = (1, 2.5, 'ranjeet', True)
# a = x + y
print(x)
print(y)
print(is_cool)
print(name)
# print(a)
# Basic Math
a = x + y
print(x, y, name, is_cool, a)

# Casting
x = str(x)
print(type(x))
y = int(y)
z = float(y)
print(type(y), y)
print(type(z), z)

