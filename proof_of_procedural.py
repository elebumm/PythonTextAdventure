from engine import Room
from map import *
import random
import time


def create_room(x,y):
        room_types = [1,2]
        algorithm = (x+y)%2
        if(algorithm ==1):
            return type_one()
        else:
            return type_two()


class type_one(Room):
    def __init__(self):
        super().__init__("typeone","type one", "")
        
class type_two(Room):
    def __init__(self):
        super().__init__("typetwo", "type two", "")


def main():
    x = game_map(2,2,4)
    location = (0,0)
    current_room = create_room(location[0],location[1])
    already_been= [(0,0)]
    already_been.append(location)
    
    while(True):
        put = input("Where will you go?\n> ")
        if (put =='n'):
            if(location[1]-1 >=0):
                location = (location[0],location[1]-1)
                if location not in already_been:
                        already_been.append(location)
            else:
                print("no option north")
            
        elif (put == 'e'):
            if(location[0]+1<x.get_width()):
                location = (location[0]+1,location[1])
                if location not in already_been:
                        already_been.append(location)
                else:
                        print("you were here already")
            else:
                print("no option east")
            
        elif (put == 's'):
            if(location[1]+1<x.get_height()):
                location = (location[0],location[1]+1)
                if location not in already_been:
                        already_been.append(location)
                else:
                        print("you were here already")
            else:
                print("no option south")
        
        elif (put == 'w'):
            if (location[0]-1>=0):
                location = (location[0]-1,location[1])
                if location not in already_been:
                        already_been.append(location)
                else:
                        print("you were here already")
            else:
                print("no option west")
        
        current_room = create_room(location[0],location[1])
        print(location)
        print(current_room.get_name())
        print(current_room.get_description())


main()
