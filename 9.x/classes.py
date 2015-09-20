# File name: classes.py
# Author: Tyler Burnham
# Date created: 9/20/2015
# Date last modified: 9/20/2015
# Python Version: 3.4

#------9.3. A First Look at Classes--------
class NewClass:
    """Doc String"""
    print("hello world")

#----------9.3.2. Class Objects-----------
class ThisClass:
    """A new simple class"""
    def world(self):
        return 'hello world'

x = ThisClass()
x.world()

# __init__ method
class newClass:
    """Testing __init__ Method"""

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def method(self):
        print("Method")

y = newClass(1,2)
print(y.arg1)
print(y.arg2)

#------9.3.3. Instance Objects----------
#Can create attributes for classes that are created
x.test = 1
for x.test in range(0,10):
    print(x.test)


#-------9.3.4. Method Objects----------
#Creating method objects
yq = y.method
yq()

#-------9.3.5. Class and Instance Variables & 9.6. Private Variables ----------
class Animals:
    test = "hello world" #Class Variable 
    def __init__(self,name):
       self.name = name  #Instance Variable
       self.__private_name = name #Pr

bird = Animals("Bird")
cat = Animals("Cat")
print(bird.name + ' ' + str(bird.test))
print(cat.name + ' ' + str(cat.test))

#---------9.5. Inheritance-------------
class Bird(Animals):

    def tweet(self):
        print("tweet")

bird2 = Bird("Pigeon")
print(bird2.name)
bird2.tweet()

#---------9.9. Iterators & 9.10. Generators & 9.11. Generator Expressions------------
def everyOther(data):
    for x in range(0,len(data)-1,2):
        yield data[x]

temp_list = [x**2 for x in range(6)]
for num in everyOther(temp_list):
    print(num)



