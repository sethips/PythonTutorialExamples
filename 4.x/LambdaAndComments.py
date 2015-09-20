# File name: LambdaAndComments.py
# Author: Tyler Burnham
# Date created: 9/12/2015
# Date last modified: 9/12/2015
# Python Version: 3.4

#Lambda Expressions
def nth_power(n):
    return lambda x: x**n

square_it  = nth_power(2)
print(square_it(1))
print(square_it(2))
print(square_it(3))
#1
#4
#9

#Docstrings
def new_function():
    """ This is an example of a doc string."""
    pass
