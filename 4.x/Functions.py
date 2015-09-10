# File name: Functions.py
# Author: Tyler Burnham
# Date created: 9/6/2015
# Date last modified: 9/6/2015
# Python Version: 3.4


#------------4.6. Defining Functions ---------------
#Create a simple function
def print_test_function():
    print("it worked")

#Test it
print_test_function()
#it worked

#Create a function with an argument
def function_with_param(thing):
    print(str(thing))

#Test it with different types
function_with_param(5)
function_with_param("This")
function_with_param([x for x in range(0,9)])
#5
#This
#[0, 1, 2, 3, 4, 5, 6, 7, 8]

#Using default args/ optional parameters
def function_with_defaults(thing, one=1, two=2):
    ans = one + two
    print(str(thing) + str(ans))

function_with_defaults("1+2=")
function_with_defaults("2+2=",2)
function_with_defaults("3+3=",3,3)
#1+2=3
#2+2=4
#3+3=6

#Positional and Keyword Arguments
function_with_defaults("Test:")     #Positional Argument
function_with_defaults(thing = "This:", two = 6) #2 Keyword Arguments
d = {'thing': 'from a dictionary:', 'one' : 12, 'two': 13}
function_with_defaults(**d) #Keyword Arguments unpacked from dictionary
#Test:3
#This:7
#from a dictionary:25


#Arguments and Dictionaries
def functions_with_args(thing, *args, **dictionary):
    print("-------------------")
    print(thing)
    print(args)
    print(dictionary)
    print("-------------------")

functions_with_args("This is a function with arguments and a dictionary",
           "arg1",
           "arg2",
           key1="one",
           key2="two",
           key3="three")
#-------------------
#This is a function with arguments and a dictionary
#('arg1', 'arg2')
#{'key2': 'two', 'key3': 'three', 'key1': 'one'}
#-------------------
