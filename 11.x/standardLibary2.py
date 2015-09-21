# File name: StandardLib.py
# Author: Tyler Burnham
# Date created: 9/20/2015
# Date last modified: 9/20/2015
# Python Version: 3.4


#--------------Output Formatting------------
import reprlib
print(reprlib.repr([x**2 for x in range(0,30)]))

import pprint
data = [(str(x) , str(y)) for x in range(0,10,2) for y in range(0,10,3)]
pprint.pprint(data, width=15)

import textwrap
string = ("Lorem ipsum dolor sit amet," + 
    "consectetur adipiscing elit," + 
    "sed do eiusmod tempor incididunt" + 
    "ut labore et dolore magna aliqua." + 
    "Ut enim ad minim veniam, quis nostrud"  + 
    "exercitation ullamco laboris nisi ut" + 
    "aliquip ex ea commodo consequat." + 
    "Duis aute irure dolor in reprehenderit" + 
    "in voluptate velit esse cillum dolore" +
    "eu fugiat nulla pariatur." + 
    "Excepteur sint occaecat cupidatat non" + 
    "proident, sunt in culpa qui officia" + 
    "deserunt mollit anim id est laborum.")

print(textwrap.fill(string, width=40))

import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')
conv = locale.localeconv()
money = 9999
print(locale.format_string("%s%.*f", (conv['currency_symbol'],
                      conv['frac_digits'], money), grouping=True))

#------------------11.2. Templating-------------------
from string import Template
t = Template('Today ${name} is feeling ${feeling}.')
print(t.substitute(name='Jim', feeling='happy'))


#------------11.3. Working with Binary Data Record Layouts------
import struct



#--------------11.4. Multi-threading-------------------------
import threading
import random

class sortList(threading.Thread):
    def __init__(self, inlist):
        threading.Thread.__init__(self)
        self.inlist = inlist
    def run(self):
        self.inlist.sort()
        print(reprlib.repr(self.inlist))
              
rand_list = random.sample(range(1000), 1000)
background = sortList(rand_list)
print(reprlib.repr(rand_list))
background.start()
print("Sorting\n")
background.join()

#------------11.5. Logging------------------
import logging
logging.debug('Debug')
logging.info('Info')
logging.warning('Warning')
logging.error('Error ')
logging.critical('Critical Error')

#---------11.6. Weak References--------------
import weakref, gc

class obj:
    def __init__(self,value):
       self.value = value

new_obj = obj(42)
d = weakref.WeakValueDictionary()
d['primary'] = new_obj
print(d['primary'].value)
del new_obj
gc.collect()
#print(d['primary'])


#-------------11.7. Tools for Working with Lists----------
from array import array
arr = array( 'i', [x for x in range(10)])
print(sum(arr))
print(arr)

from collections import deque
dq = deque(["1","2","3"])
dq.append('10')
print(dq)
print(dq.popleft())

import bisect
y = [(x,y) for x in range(4) for y in range(4) if x!=y]
pprint.pprint(y, width=15)
bisect.insort(y, (2, 2))
print("After Addition")
pprint.pprint(y, width=30)

from heapq import heapify, heappop, heappush
q = [9,13,5,7,2,4,6]
heapify(q)
heappush(q,100)
print([heappop(q) for i in range(6)])

#----------------11.8. Decimal Floating Point Arithmetic---------
from decimal import *
getcontext().prec = 5

print(round(Decimal('.6')*Decimal('1.15'),3))
print(round(.6*1.15,3))

print("-------")
print(Decimal('2.00') % Decimal('.2'))
print(2.00%.2)

print(Decimal(1) / Decimal(13))
