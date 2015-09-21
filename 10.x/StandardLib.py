# File name: StandardLib.py
# Author: Tyler Burnham
# Date created: 9/20/2015
# Date last modified: 9/20/2015
# Python Version: 3.4

#------10.1. Operating System Interface-------
import os
print(os.getcwd())
os.chdir('C:/')
print(os.getcwd())
#print(os.system('cmd'))

#----------10.2. File Wildcards-------------
import glob
print(glob.glob(r'C:\Users\42\Documents\GitHub\PythonTutorialExamples\10.x\*.py'))


#-----10.3. Command Line Arguments----------
import sys
#print(sys.argv)

#-----10.4. Error Output Redirection and Program Termination----------
sys.stderr.write('Writing to the error stream\n')


#--------10.5. String Pattern Matching-----------------
#Regular expressions
import re
print(re.findall(r'\bj[a-z]*', 'A quick brown fox jumps over the lazy dog.'))


#-------10.6. Mathematics-----------------------
import math
print(math.pi)
print(20*math.log(1000, 10))

import random
print(random.choice([x**2 for x in range(5,10)]))
print(random.sample(range(10), 10))
print(random.random())
print(random.randrange(100))

import statistics
data = random.sample(range(50), 15)
print(data)
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))

#-------------10.7. Internet Access--------------
from urllib.request import urlopen
with urlopen('https://docs.python.org/3.4/tutorial/stdlib.html#mathematics') as response:
    for line in response:
        line = line.decode('utf-8')
        if 'internet' in line:
            print(line)



#-----------10.8. Dates and Times------------------
from datetime import date
print(date.today())
print(date(1994, 7, 19))
print(date.today().strftime("%m-%d-%y"))
print(str(date.today()-date(1994, 2,17)))

#-----------10.9. Data Compression---------------
import zlib
s = b'The quick brown fox jumps over the lazy dog.'
compressed = zlib.compress(s)
print(s)
print(compressed)
print(zlib.decompress(compressed))


#-----------10.10. Performance Measurement--------
from timeit import Timer
print(Timer("z.sort()", 'z=[x for x in range(0,1000)]').timeit())


#----------10.11. Quality Control------------------
def test():
    """
    >>> print(test())
    42
    """
    return 42

import doctest
print(doctest.testmod())
