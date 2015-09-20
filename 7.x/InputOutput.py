# File name: InputOutput.py
# Author: Tyler Burnham
# Date created: 9/20/2015
# Date last modified: 9/20/2015
# Python Version: 3.4

import math

#------7.1. Fancier Output Formatting----------
#Simple Print
print('Simple')

#Print any object as string
i = 'hello \n world'
print(str(i))

#Print interpreter 
print(repr(i))

#Using rjust
for x in range(0, 10):
    print(repr(x).rjust(3), end = ' ')
    print(repr(x*2).rjust(3), end =' ')
    print(repr(x*3).rjust(3))


#Using zfill
for x in range(0,10):
    print(str(x).zfill(2))

#String Fromat
s = ('hello', 'world')
print("{} this is {}".format(s[0],s[1]))

#--------7.1.1. Old string formatting--------
#Printf Style Formatting
print('%00e' %10000000)


#-----7.2.1. Methods of File Objects------------
#File Objects

#Create File Object
file = open('test.txt', 'a+')

#write to file
text = ["writing", "to", "a", "simple", "text", "file"]
for x in text:
    file.write(str(x)+'\n')

#Print entire file
file.seek(0)
print('\nEntire contents:')
print(file.read())


#close file
file.close()

