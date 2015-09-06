# File name: Lists.py
# Author: Tyler Burnham
# Date created: 9/6/2015
# Date last modified: 9/6/2015
# Python Version: 3.4

#--------Section 3.1.3 Lists-----------

#Create Lists
print("Create Lists")
squares  = [x**2 for x in range(0,11)] #Create a list of squares
cubes = [x**3 for x in range(0,11)] #Create a list of cubes
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(cubes) # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]]

#Retrieve List Elements
print("Retrieve List Elements")
print(squares[-1]) #get the last element: 100
print(squares[-2:]) #get the last 2 elements: [81, 100]
print(squares[-2:]+cubes[-2:]) #concatenation of both lists  [81, 100, 729, 1000]

#Update Lists
print("Update Lists")
squares[0] = -1 #Can change lists by location 
print(squares) #[-1, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

squares[0:3] = cubes[4:9] #Can modify ranges
print(squares) #[64, 125, 216, 343, 512, 9, 16, 25, 36, 49, 64, 81, 100]

squares.append(99) #Can append to list
print(squares) #[64, 125, 216, 343, 512, 9, 16, 25, 36, 49, 64, 81, 100, 99]

#Nested Lists
first = ['f','i','r','s','t']
seccond = "S E C C O N D".split() #Split a string with the .split function
both = [first,seccond] #Make a nested list with two lists
print("Nested Lists")
print(both) #[['f', 'i', 'r', 's', 't'], ['S', 'E', 'C', 'C', 'O', 'N', 'D']]
print(both[1][1]) # E


#-----------Practical Application--------------
print('Application')

#Replace the current char in a nested list      
def grid_save(x,y,grid,newWord):
    if(x <= len(grid)-1 and y <= len(grid[x]) -1):
        grid[x][y] = newWord

#Simulate Tic-Tac-Toe
grid = [['_','_','_'],['_','_','_'],['_','_','_']]
grid_save(0,0,grid,'x')
grid_save(2,2,grid,'o')
grid_save(1,0,grid,'x')
grid_save(1,2,grid,'o')
grid_save(1,1,grid,'x')
grid_save(0,2,grid,'0')

#Print the final grid
for row in grid:
    print(row)



