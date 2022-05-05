#Challenge:
#Compute Area and Perimeter
#Medium
#Problem Description
#Create a program to compute the area and perimeter of a square using class. If you don't know, a square is a rectangle with equal sides.

class Square:

    
    def __init__(self, length):
        self.length = length 
    
    def get_area(self):
        return self.length ** 2
        
    def get_perimeter(self):
        return self.length * 4 


# get integer 
length = int(input())

# create an object of Square    
s1 = Square(length)

# call get_area() and print the area
print(s1.get_area())

# call get_perimeter() and print the perimeter
print(s1.get_perimeter())
