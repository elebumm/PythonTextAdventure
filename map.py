import time
import random

class game_map:




    ##initialize
    height,width,room_tot = 0,0,0
    map_grid = [[0]]
    
    def __init__(self,w,h,rn): ##initialize grid, heihgt width and room tot
        self.width = w
        self.height = h
        self.room_tot = rn
        self.map_grid = [[False]*self.height for _ in range(self.width)]

    def generate_map(self):
         
        room_count=1
        start = (int(self.width/2-1),int(self.height/2-1))
        self.map_grid[start[0]][start[1]] = True
        current = start
        print("starts here ", start)
        
        while (room_count < self.room_tot):
            
            d = [0,1,2,3]
            nxt = random.randint(0,3)

            direction = [(current[0],current[1]+1),(current[0]+1,current[1]),(current[0],current[1]-1),(current[0]-1,current[1])]
            new_curr = direction[nxt]
            
            if (new_curr[0]<self.width and new_curr[0] >= 0):
                if(direction[nxt][1]<self.height and direction[nxt][1] >=0):
                    
                    if (self.map_grid [direction[nxt][0]] [direction[nxt][1]] != True):
                        
                        self.map_grid [direction[nxt][0]] [direction[nxt][1]] = True
                        current = direction[nxt]
                        room_count = room_count+1
                        print(room_count)
                        
                        
                    else:
                        current = direction[nxt]
            else:
                pass##fill in later

    def print(self):
        for j in range(0,self.width):
            if (j!=0):
                print('\n')
            for i in range(0,self.height):
                print(self.map_grid[j][i], end = " ")

def main():
    x = game_map(4,4,4)
    x.generate_map()
    x.print()
