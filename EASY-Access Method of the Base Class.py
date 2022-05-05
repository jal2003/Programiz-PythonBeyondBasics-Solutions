# Challenge:
# Access Method of the Base Class
# Easy
# Problem Description
# Create a program to call the method of the base class using an object of the derived class.

#the Animal class
class Animal:
    def eat(self):
        print('I can eat food')
#the Dog class
class Dog(Animal):
    def bark(self):
        print('I can bark')

#object of Dog
dog1 = Dog()


# call using the object
dog1.eat()
