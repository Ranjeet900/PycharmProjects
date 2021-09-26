# Q.1 How would you confirm that 2strings have the same identity?
'''
animals = ['python', 'gopher']
more_animals = animals

print(animals == more_animals)
print(animals is more_animals)

even_more_animals = ['python','gopher']

print(animals == even_more_animals)
print(animals is even_more_animals)
'''

# Q.2 How would you check if each word in a string begins with a capital letter?
'''
print('My Name'.istitle())
print('ranjeet Kumar'.istitle())
print('wHat is'.istitle())
print('are IS'.istitle())
print('HeLLO'.istitle())
print('IaS'.istitle())
'''
# Q3. Check if a string contains a specific substring
# The in operator will return True if a string contains a substring.
'''
print('plane' in 'The worlds fastest plane')
print('car' in 'The worlds fastest plane')
'''

# Q4. Find the index of the first occurrence of a substring in a string
# There are 2 different functions that will return the starting index ,find() and index().
# find() returns -1 if the substring is not found.
'''
print('The worlds fastest plane'.find('plane'))
print('The worlds fastest plane'.find('car'))
'''

# Q.5 Count the total numbers of characters in a string.
# len() will return the length of the string.
'''
My_Message = 'Hello!, How are you doing?'
print(len(My_Message))
print(My_Message)
print(My_Message.count('o'))
'''
# Q.6 Count the numbers of a specific character in a string.
# Count() will return the numbers of the occurrences  of a specific character.

My_Message = 'Hello!, How are you doing?'
print(My_Message.count('o'))

# Q.7 Capitalize the first character of a string.
# Use the capitalization() function to do this.
Hi_all = 'rat race,fish,cat'
print(Hi_all.capitalize())

# Q.8 what is an f-string and how do you use it?
# New in python 3.6 , f-strings make string interpolation  really easy. Using f-strings is similar to using format()
name ='Ranjeet Kumar'
food = 'Paw bhaji'
print(f'Hello. My name is {name} and I like {food}')

# Q.9 Search the specific part of the string for a substring.
# Index can also be provided with optional start and end indices for searching within a large string.

print('the happiest person in the whole wide world.'.index('the',10,44))

# Q.10 Interpolate a variable into a string using format()
# format() is similar to using an f-string.

difficulty = 'easy'
thing = 'exam'
print('That {} was {}!'.format(thing, difficulty))



















