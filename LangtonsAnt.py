#Author: Christian Augustyn
#File Name: LangtonsAnt.py 
#Date: Feb 7, 2018
#Summary: Moves an "ant" base of a set of decisions to create a pattern

import sys, pygame

class Ant:
    
    def __init__(self, x, y, dir, grid): # creates an object with an(x, y) pos, the directio tne ant is facing and the state of the square the ant is on
        self.x = x
        self.y = y
        self.dir = dir  #starting direction
        self.grid = grid
        self.ANTUP, self.ANTRIGHT, self.ANTDOWN, self.ANTLEFT = 0, 1, 2, 3
        
    def turnRight(self):
        self.dir += 1
        
        if (self.dir > self.ANTLEFT):
            self.dir = self.ANTUP
    
    def turnLeft(self):
        self.dir -= 1
        
        if (self.dir < self.ANTUP):
            self.dir = self.ANTLEFT
            
    def moveForward(self):
        if (self.dir == self.ANTUP):
            self.y -= 1
            
            
        elif (self.dir == self.ANTRIGHT):
            self.x += 1
            
        elif (self.dir == self.ANTDOWN):
            self.y += 1
            
        elif (self.dir == self.ANTLEFT):
            self.x -= 1
            
    def setState(self, newColor):
        self.grid[self.y][self.x] = newColor
    
    def printArray(self):
        for row in self.grid:
            for element in row:
                print(element, end=" ")
            print()
        print()
            
    def checkBounds(self):
        if (self.dir == self.ANTUP):
            print("ANTUP")
            if (self.x == 0) and (self.grid[self.y][self.x] == "X"):
                return False
            
            elif (self.x == len(self.grid) - 1) and (self.grid[self.x][self.y] == " "):
                return False
            
            else:
                return True
            
        elif (self.dir == self.ANTRIGHT):
            print("ANTRIGHT")
            if (self.y == 0) and (self.grid[self.y][self.x] ==  "X"):
                return False
            
            elif (self.y == len(self.grid) - 1) and (self.grid[self.x][self.y] == " "):
                return False
            
            else:
                return True
            
        elif (self.dir == self.ANTDOWN):
            print("ANTDOWN")
            if (self.x == 0) and (self.grid[self.y][self.x] == " "):
                return False
            
            elif (self.x == len(self.grid) - 1) and (self.grid[self.y][self.x] == "X"):
                return False
            
            else:
                return True
            
        elif (self.dir == self.ANTLEFT):
            print("ANTLEFT")
            if (self.y == 0) and (self.grid[self.y][self.x] == " "):
                return False
            
            elif (self.y == len(self.grid) - 1) and (self.grid[self.y][self.x] == "X"):
                return False
            
            else:
                return True
            
    def run(self):
        if (self.grid[self.y][self.x] == " "):
            self.setState("X")
            self.turnRight()
            self.moveForward()
        else:
            self.setState(" ")
            self.turnLeft()
            self.moveForward()

def genArray(length):
    array = []
    for y in range(0, length):
        array.append([])
        for x in range(0, length):
            array[y].append(" ")
    return array
            
#initial variables needed for Ant class   
length = 100
grid = genArray(length)
direction = 0
ant = Ant(50, 50, direction, grid)

#Initial Variables needed for pygame
size = length, width = 1000, 1000
white = 255, 255, 255
black = 0, 0, 0
clock = pygame.time.Clock()
window = pygame.display.set_mode(size)
tile = 10
pygame.display.set_caption("Langton's Ant Simulation")

#Game loop
inBounds = True
while inBounds is True:
    inBounds = ant.checkBounds()
    ant.run()
    #if pygame is not installed replace all code below with ant.printArray()
    #this will create a view in the console instead

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    window.fill(white)
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            rect = pygame.Rect((x * tile, y * tile),(tile ,tile))
            if ant.grid[y][x] == " ":
                pygame.draw.rect(window, white, rect)
            
            elif ant.grid[y][x] == "X":
                pygame.draw.rect(window, black, rect)
                
    pygame.display.update()
    clock.tick(60)


    
    



    






            
