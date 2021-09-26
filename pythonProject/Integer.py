# Arithmetic operators:
# Addition : 3 + 3
# Subtraction : 3 - 2
# Multiplication : 3 * 2
# Division : 3 / 2
# Floor Division : 3 // 2
# Exponent : 3 ** 2
# Modules : 3 % 2
# ------------------------------------------------------------------------
# Addition : 3 + 3
"""
print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2)
print(3 % 2)
print(3 ** 2)
"""
# Create a dictionary  and take input from the user and return the meaning of the word from the dictionary
"""
user = input('Enter the word!')
name = {'set': 'This is a list of the elements','History': 'Where you learned from past things', 'production':'the form of production where you make product in a factory'}
"""
# Set
# cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
# art_courses = {'History', 'Math', 'Art', 'design'}
# print(cs_courses.intersection(art_courses))
# # print(cs_courses)
# # print(help(set))


# Iterator & iterables
nums = [1,2,3,5,4]
# for num in nums:
#     print(num)
# print(dir(nums))

it = iter(nums)
print(it.__next__())

print(next(it))

for i in nums:
    print(i)




