# print("Hi")
"""
Creating the class dog.
"""
# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def sit(self):
#         print(f"{self.name} is sitting now.")
#     def roll_over(self):
#         print(f"{self.name} rolled over.")




# class myClass():
#     def method1(self):
#         print('myClass Method1')
#     def method2(self ,someString):
#         print("myClass method2" + someString)
#     def main(self):
#         c = myClass()
#         c.method1()
#         c.method2("This is a string")
#
#
# if __name__ == "__main__":
#     main()


# class  Fruit:
#     def __init__(self):
#         self.name = "Apple"
#         self.color = "red"
#         print(f"My fruit name is {self.name} and it's color is {self.color}")
#
# my_fruit = Fruit()

class Fruit:
    def __init__(self,name,clr):
        self.name = name
        self.clr = clr
    def details(self):
        print("my " + self.name + " is " + self.clr)
apple = Fruit("apple", "red")
apple.details()

























