#Challenge:
#Exception Handling With Lists
#Easy
#Problem Description
#Create a program to print the item present at a given index. If the index is out of bounds, print Wrong index.

try:
    cars = ['BMW', 'Ferrari', 'Audi', 'Tesla']

    # take integer input
    index = int(input())

    # print the item from the cars list
    print(cars[index])
    
except:
    print("Wrong Index")
