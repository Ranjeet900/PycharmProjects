""""
String in python are surrounded by either single or double quotation marks.
Look at string formatting and some string methods.
"""

# name = 'Brad'
# age = 22
#
# #  Concatenate
# print('Hello, my name is ' + name + ' and I am ' + str(age))
#
# # Arguments by position
# print(f'My name is {name} and I am {age}'.format(name = name , age = age))
#
# # F-strings (3.6 and after python versions)
# print(f"Hello, my name is {name} and I am {age}")

#  String Methods
s = 'helloworld'

# capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# make all lower
print(s.lower())

# swap case
print(s.swapcase())

# Get length
print(len(s))

# replace

print(s.replace('world', 'Universe'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find Position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())

print('Hello, How are you?')











