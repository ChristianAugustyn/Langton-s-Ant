  
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
            
   
length = 100
grid = genArray(length)
direction = 0
ant = Ant(50, 50, direction, grid)

inBounds = True
while inBounds is True:
    inBounds = ant.checkBounds()
    ant.run()
    ant.printArray()
    
    



    






            
