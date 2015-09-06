# File name: FirstSteps.py
# Author: Tyler Burnham
# Date created: 9/6/2015
# Date last modified: 9/6/2015
# Python Version: 3.4

#--------3.2. First Steps Towards Programming-----------

#This is a small section of the tutorial showing how to get a basic program
#They demonstrate
    #While loops
    #Print Statements
    #Multiple Assignments
    #Indention

#Here is a small example oing somthing different then the tutorial

low, high = 5, 100 #Multiple Assignments

#Count down from the difference of var1 and var2
while(low < high):
    print(high-low)
    high , low = high + 1, low + 2 #Multiple Assignments

#Prints 95->1
