# File name: errors.py
# Author: Tyler Burnham
# Date created: 9/19/2015
# Date last modified: 9/19/2015
# Python Version: 3.4

#--------8.1. Syntax Errors----------
#for x in range(10)

#--------8.2. Exceptions---------------
#Divide by zero (ZeroDivisionError)
#x = 1/0

#Undefined Variable (NameError)
#y = foo*5

#Conversion (TypeError)
#z = "two" + 123

#------8.3. Handling Exceptions---------
#Using the except statement
try:
    x = 1/0
except ZeroDivisionError:
    print("cant divide by zero")

#Multiple Exceptions
try:
    x = int(input())
except (ZeroDivisionError, ValueError) as err:
    print(err)

#---------8.4. Raising Exceptions & 8.5. User-defined Exceptions----------
#Create a test exemption
class TestError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#Call the exemption
try:
    raise TestError("It Broke")
except TestError as err:
    print("Error: " + str(err))

#----8.6. Defining Clean-up Actions &8.7. Predefined Clean-up Actions------
try:
    c = 1/0
except ZeroDivisionError:
    print("Divide by zero")
finally:
    print("Clean Up")

#using with and as
with open("textfile.txt") as flie
    print(file.read())
    
