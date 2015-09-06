# File name: Numbers.py
# Author: Tyler Burnham
# Date created: 9/5/2015
# Date last modified: 9/5/2015
# Python Version: 3.4

#Basic Math Opperations section 3.1.1
math = []
math.append(2+3) #2+3=5
math.append(2-3) #2-3=-1
math.append(2*3) #2x3=6
math.append(2/3) #2/3= 1/3
math.append(2//3)#integer devide 2/3 = 0 
math.append(2%3) #2 mod 3 = 2
math.append(2**3)#2 to power of 3 = 8

print("Answers:") 
print(math) #[5, -1, 6, 0.6666666666666666, 0, 2, 8]

# Practical Application
def Fahrenheit_To_Celsius(F):
    return ((F - 32) * 5/9)

print("Fahrenheit To Celsius: ")
print("F(-10)=" + str(Fahrenheit_To_Celsius(-10)))
print("F(32)=" + str(Fahrenheit_To_Celsius(32)))
print("F(50)=" + str(Fahrenheit_To_Celsius(50)))
print("F(100)=" + str(Fahrenheit_To_Celsius(100)))
#Fahrenheit To Celsius: 
#F(-10)=-23.333333333333332
#F(32)=0.0
#F(50)=10.0
#F(100)=37.77777777777778
