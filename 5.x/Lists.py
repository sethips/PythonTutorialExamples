# File name: Lists.py
# Author: Tyler Burnham
# Date created: 9/12/2015
# Date last modified: 9/19/2015
# Python Version: 3.4

from collections import deque

# ---------- 5.1. More on Lists ------------------
cubes = [0, 1, 27, 64, 125, 216, 343, 512, 729]

#Append
cubes.append(1000)

#Insert
cubes.insert(2, 8)

#Index
print("Cubes index of 343 = " + str(cubes.index(343))) #index = 7 
print(cubes)

#Create temp List
unordered = [4, 2, 1, 0, 3]
print("List = " + str(unordered))

#Reverse List
unordered.reverse()
print("Reverse = " + str(unordered))

#Sort List
unordered.sort()
print("Sorted = " + str(unordered))

# ---------- 5.1.1. Using Lists as Stacks ---------------
stack = [1,2,3]
stack.append(4) #[1,2,3,4]
stack.append(5) #[1,2,3,4,5]
stack.pop()     #[1,2,3,4]
print(stack)
#[1,2,3,4]


# ---------- 5.1.2. Using Lists as Queues-----------------
queue = deque(["First","Seccond"])
queue.append("Third")
print(queue)

queue.popleft()
print(queue)

# ---------- 5.1.3. List Comprehensions-----------------
#Simple List Comprehension
simple = [x+1 for x in range(10)]
print(simple)

#Tuple List comprehension
arrayList = [(x,y) for x in range(0,10) for y in range(0,10) if x==y]
print(arrayList)

#Filtering with list comprehension
seq = [1,2,3,4,5,6,7,8,9,10]

#Square list
print([x**2 for x in seq])

#filter greater then 5
print([x for x in seq if x>5])

#apply function or method
print([ hex(x) for x in seq])


#---------5.1.4. Nested List Comprehensions-----------
#Simple Nested List Comp
print([[x for x in range(4)] for i in range(4)])


#------------5.2. The del statement------------
arr = [0,1,2,3,4]
del arr[0]
print(arr)
del arr[1:2]
print(arr)

#-----------5.3. Tuples and Sequences----------------
#Tuples can be any length but are immutable
t = (1,2,3)
print(t[0])

t2 = (1,2,3,4,5)
print(t2[4])

#-----------5.4. Sets---------------
a = {'a','b','1','2'}
b = {'a','a','b',';',':'}

#Letters in a not b
print(a - b)

#Letters in both a and b
print(a | b)

#Letters in a and b
print(a & b)

#Letters in a or b not both
print(a ^ b)


#----------------5.5. Dictionaries------------------
dictA = {'thing1': 1, 'thing2': 2}
print(dictA)
print(dictA['thing1'])
print('thing1' in dictA) 
print(dictA.keys())

#---------------5.6. Looping Techniques-------------
#loop through dictionaries
for i, j in dictA.items():
    print(i, j)

#Enumerate function
for i, j in enumerate([ x**2 for x in range(10)]):
    print(i,j)

#Reversed Function
for i in reversed(range(0,5)):
    print(i)

#Sorted Function
for i in sorted(['b','a','c']):
    print(i)





