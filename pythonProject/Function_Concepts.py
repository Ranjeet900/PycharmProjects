# print('hello')
# def My_name(username):
#     print(f"hello, {username.title()}!")
# My_name('Ranjeet Kumar')
'''
Q1.) Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter.
call the function, and make sure the message displays correctly

'''
# def display_message(message):
#     print(f"Hi,{message.title()}!")
# display_message('In this chapter you will learn about functons and thier parametrs as well arguments')

"""
Keyword Arguments!
"""
# def describe_pet(pet_name ,animal_type ='dog'):
#     """ Display information about a pet."""
#     print(f'\n I have a {animal_type}.')
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# # describe_pet(animal_type= 'GermanSheferd' ,pet_name= 'Sheru' )
# # describe_pet(animal_type= 'StreetDog' ,pet_name= 'Milky' )
# # describe_pet(animal_type= 'LabraDog' ,pet_name= 'Sheru' )
# # describe_pet(animal_type= 'SniferDog' ,pet_name= 'Rocky' )
# # describe_pet(animal_type= 'GermanSheferd' ,pet_name= 'Sheru' )
# # describe_pet(animal_type= 'GermanSheferd' ,pet_name= 'Sheru' )
# describe_pet(pet_name= 'Sheru' )
# describe_pet(pet_name= 'Sheru' )
# describe_pet(pet_name= 'Sheru' )
# describe_pet(pet_name= 'Sheru' )
# describe_pet(pet_name= 'Sheru' )


"""
Q2.) Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.
"""
# def favourite_book(book):
#     print(f'I like to read a book and her name is {book.title()}')
# favourite_book('Alchamists')

"""
Q3.) T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""
# def make_shirt(size , message):
#     print(f'\n The shirt size are {size.title()}and It is one of the best shirt in my shop and It is a rarest collection{message.title()}')
#
# make_shirt('M ' ,'and not too costly.')

"""
Q4.) Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
"""
# def make_shirt(message ,message1 = 'Python ', size = 'M '):
#     print(f'\n The shirt size are {size}and It is one of the best shirt in my shop and It is a rarest collection{message}')
#     print(f'I love {message1.title()}')
#
# make_shirt(' not too costly.')

"""
Q5.) Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.
"""
# def describe_city(city , country ='India'):
#     print(f'Describe the city:{city.title()} is the part of {country}')
# describe_city(' New delhi')
# describe_city(' Bihar')
# describe_city(' Mumbai')

"""
Return function:
"""
# def get_formatted_name(first_name , last_name):
#     """ Return a full name , neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# Software_developer = get_formatted_name('Ranjeet','Kumar')
# print(Software_developer)

"""
Making an argument optional
"""
# def get_formatted_name(first_name , last_name,middle_name =''):
#     """ Return a full name , neatly formatted."""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     # full_name = f"{first_name} {last_name}"
#     return full_name.title()
# Software_developer = get_formatted_name('Ranjeet','Kumar')
# print(Software_developer)
# Software_developer = get_formatted_name('Ranjeet','Kushwaha','Kumar')
# print(Software_developer)

"""
Returning a Dictionary
"""
# def built_person(first_name , last_name ,age =None):
#     """ Returning a dictionary of information about person."""
#     person = {'first': first_name ,'last': last_name}
#     if age:
#         person['age'] = age
#     return person
# software = built_person('Ranjeet' , 'Kumar' , age=22)
# print(software)
#

"""Using a function with a while loop"""
# def get_formatted_name(first_name , last_name):
#     """ Return a full name , neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# # This is an infinite loop!
# while True:
#     print("\n Please tell me your name:")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First name:")
#     if f_name == 'q':
#         break
#     l_name = input("Last name:")
#     if l_name == 'q':
#         break
#     formatted_name = get_formatted_name(f_name,l_name)
# print(f"\nHello, {formatted_name}!")
#
"""
City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the
values that are returned
"""

"""
Passing a list
"""
# def greet_user(names):
#     for name in names:
#         msg = f"Hello,{name.title()}"
#         print(msg)
# usernames = ['Ram','Mohan','Sohan']
# greet_user(usernames)
#
"""
Modifying a list in a function
"""
# unprinted_designs = ['phone case', 'robot pendent', 'dodecahedron']
# completed_models = []
# while unprinted_designs:
#     current_design= unprinted_designs.pop()
#     print(f'Printing model: {current_design}')
#     completed_models.append(current_design)
# print("\n The following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

"""
Passing an arbitrary numbers of arguments
"""
# def make_pizza(*toppings):
#     print("\n Making a pizza with the following toppings.")
#     for topping in toppings:
#       print(f"-{topping}")
# make_pizza('papperoni')
# make_pizza('mushrooms','green peppers','extra cheese')

"""
Using Arbitrary Keyword Arguments
"""
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)



















