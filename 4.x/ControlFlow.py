# File name: Lists.py
# Author: Tyler Burnham
# Date created: 9/6/2015
# Date last modified: 9/6/2015
# Python Version: 3.4

import random

#-------4.1 If Statements--------------
#Here is a simple example using if,else if, and else.
#It simulates a coin toss saying if you won or loss
value = round(random.random()*1000)
print(value)
if(value>500):
    print("You Win")
elif(value<500):
    print("You Lose")
else:
     print("Almost")


#-------4.2 For Statements--------------

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
print("The first " + str(len(primes)) + " primes are:")
#Simple For Statement to print the primes list
for x in primes:
    print(x)

#For loop not affecting the list
print("Primes +1 Showing list is unaffected")
for x in primes:
    x+=1
    print(x)
print(primes)

#-------4.3 Range Function--------------
#Using Range with a for loop
numbers = []
for x in range(0,100,5):
    numbers.append(x)
print(numbers)
#[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

#Using range casting it to a list
del numbers
numbers = list(range(0,100,10))
print(numbers)
#[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

#-------4.5 Pass Function--------------
#Example of using pass as a place holder
for x in range(0,10):
    pass #Need to Finish
