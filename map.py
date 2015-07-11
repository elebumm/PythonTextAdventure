import time
import random

class game_map:

    ##initialize
    height,width,room_tot = 0,0,0
    map_grid = [[0]]
    past_location = [(0,0)]
    
    def __init__(self,w,h,rn): ##initialize grid, heihgt width and room tot
        self.width = w
        self.height = h
        self.room_tot = rn
        self.map_grid = [[False]*self.height for _ in range(self.width)]##initializes grid as all false
        
    def generate_map(self):
         
        room_count=1
        start = (int(self.width/2-1),int(self.height/2-1))
        self.map_grid[start[0]][start[1]] = True
        current = start
        ##starts the grid with one point
        
        while (room_count < self.room_tot):
            
            d = [0,1,2,3]
            nxt = random.randint(0,3)##rand int

            direction = [(current[0],current[1]+1),##all possible directions relative to current position
                         (current[0]+1,current[1]),
                         (current[0],current[1]-1),
                         (current[0]-1,current[1])]##better? :P
            
            new_curr = direction[nxt]
            
            if (new_curr[0]<self.width and new_curr[0] >= 0):
                if(direction[nxt][1]<self.height and direction[nxt][1] >=0):##new direction is in bounds
                    
                    if (self.map_grid [direction[nxt][0]] [direction[nxt][1]] != True):##doesnt count if already true
                        
                        self.map_grid [direction[nxt][0]] [direction[nxt][1]] = True##flips bool thus "creating a room"
                        current = direction[nxt]
                        room_count = room_count+1
                        
                    else:
                        current = direction[nxt]##move on otherwise
            else:
                pass#out of bounds exception



    def __str__(self):##str basic print func
        for j in range(0,self.width):
            if (j!=0):
                print('\n')
            for i in range(0,self.height):
                print(self.map_grid[j][i], end = " ")

    def get_width(self):##return funcs
        return self.width

    def get_height(self):
        return self.height
    
                
    def print(self):##slightly prettier print, which prints only active rooms in the order they will be
        for j in range(0, self.width):
            print('\n')
            print("      "*self.width)
            for i in range(0,self.height):
                print(" ",end="")
                
                if (self.map_grid[j][i]==False):##white spice for false
                    print("    ",end = "")
                else:
                    print(self.map_grid[j][i],end="")##true for true nut can be replaced witha graphic
                print(" ",end = "")

    
        
        

def main():
    x = game_map(10,10,9)
    print("rooms: ",x.room_tot)
    print("grid: ", x.width, " x ", x.height)
    
    x.generate_map()
    x.print()

main()
