# File name: Strings.py
# Author: Tyler Burnham
# Date created: 9/6/2015
# Date last modified: 9/6/2015
# Python Version: 3.4

#--------Section 3.1.2. Strings-----------
strings = []
strings.append('Hello World') #Simple string single quotes
strings.append("Hello World") #Simple string double quotes
strings.append("\"Escape Chars\"") #Escaping Quotes
strings.append(r'C:\Windows\System32') #Raw String ignores escapes
strings.append("""
This
Is
A
Multi-Line
Quote
""")
strings.append('na ' * 16 + 'Batman!') #Repeating strings and concatenation
word = 'ABCDEFG'
strings.append(word[2]) #get the character at 2. word[2] = 'C'
strings.append(word[2:4]) #gets a range from 2 up to 4. word[2:4] = 'CD'
strings.append(word[-3:]) #gets a range from third to last to the end. word[-3:] = 'EFG'
strings.append(word[::-1]) #gets reverses string. word[::-1] = 'GFEDCBA'

strings.append("Length=" + str(len(word))) #Gets the length of the string

for example in strings:
    print(example)

#------Output--------
#Hello World
#Hello World
#"Escape Chars"
#C:\Windows\System32
#
#This
#Is
#A
#Multi-Line
#Quote
#
#na na na na na na na na na na na na na na na na Batman!
#C
#CD
#EFG
#GFEDCBA



#practical application
def is_it_a_palindrome(word):
    print(word)
    print(word[::-1])
    word = word.strip().replace(" ", "")
    print('Palindorme!' if word == word[::-1] else 'Not Palindrome')
    print('')

print("--------------")
is_it_a_palindrome('doc note i dissent a fast never prevents a fatness i diet on cod')
is_it_a_palindrome('racecar')
is_it_a_palindrome('Tyler Burnham')

#---------Output-----------
#doc note i dissent a fast never prevents a fatness i diet on cod
#doc no teid i ssentaf a stneverp reven tsaf a tnessid i eton cod
#Palindorme!
#
#racecar
#racecar
#Palindorme!
#
#Tyler Burnham
#mahnruB relyT
#Not Palindrome
