################################################################################################
#
# Use this as a reference for importing. Instead of "from gamemap import *" use:
#
# from gamemap import GameMap, Floor, RandomFloor
#
# IN THIS MODULE:
#
# CLASSES:
#   * GameMap (Node)
#       * Floor (GameMap)
#       * RandomFloor (GameMap)
#
# METHODS:
#
#
################################################################################################

import time
import random
from node import Node, Leaf, node_search, node_search_deep, node_move
from room import Room

class GameMap(Node):

    # MAP SIZE INITIALIZATION
    def __init__(self, name, description, width, height):
        Node.__init__(self, name, description)
        
        self.width = width if width >= 0 else -width
        self.height = height if height >= 0 else -height
            
        self.map_grid = [[False]*self.height for row in range(self.width)]

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return "This floor is " + str(self.height) + " cells tall by " + str(self.width) + " cells wide. Total Area: " + str(self.height * self.width)

    # Rooms // wraps Node children methods
    def add_room(self, room, coordinate):
        Node.add_child(self, room)
        self.map_grid[coordinate[0]][coordinate[1]] = room

    def remove_room(self, room, coordinate):
        Node.remove_child(self, room)
        self.map_grid[coordinate[0]][coordinate[1]] = False

    def list_rooms(self): #lists floor Room objects
        Node.list_children(self)

    ## MAP VISUALIZATION
    def correct_map_orientation(self): # Rotate map 90 degrees counterclockwise.
        wrong_map = self.map_grid
        correct_map = []

        for p in range(0, self.height):
            row = []
            for q in range (0, self.width):
                row.append(wrong_map[q][p])
            correct_map.append(row)

        correct_map = list(reversed(correct_map))

        self.map_grid_corrected = correct_map # map_grid_corrected is only for visualization! use map_grid for other non-visual activites

    def view_map(self, room = "#", empty = u"\u25A1", border = u"\u25A0"): # Display the map in correct orientation

        self.correct_map_orientation() # Generate visually correct map matrix

        for i in range(0, self.height + 2): # Top Border
            print(border, end = " ")
        print() # newline
        
        for j in range(0, self.width): # Map Cells

            print(border, end = " ") # left border

            for i in range (0, self.height): # Print out map cell symbols

                ## Add conditions here for map markers. For example
                ## if Player.position = (j, i)
                if self.map_grid_corrected[j][i] == "Start":
                    print("S", end = " ")
                elif self.map_grid_corrected[j][i] == "End":
                    print("E", end = " ")
                elif isinstance(self.map_grid_corrected[j][i], Room):
                    print("R", end = " ")
                elif self.map_grid_corrected[j][i]:
                    print(room, end = " ")
                else:
                    print(empty, end = " ")

            print(border) #right border
            
        for i in range(0, self.height + 2): # Bottom Border
            print(border, end = " ")
        print("\n") # 2 newlines

class Floor(GameMap):

    # MAP GENERATION
    def __init__(self, name, description, width, height):
        GameMap.__init__(self, name, description, width, height)

    def map_rooms_to_cell(self, rooms, coordinates):
        for c in range(0, len(coordinates)):
            self.add_room(rooms[c], coordinates[c])

class RandomFloor(GameMap):

    # MAP GENERATION
    def __init__(self, name, description, width, height, desired_room_quantity):
        GameMap.__init__(self, name, description, width, height)
        self.set_total_rooms(desired_room_quantity)

    def set_total_rooms(self, desired_room_quantity):

        self.total_rooms = desired_room_quantity if desired_room_quantity >= 0 else -desired_room_quantity

        if self.total_rooms <= (self.width * self.height):
            self.map_grid = [[False]*self.height for row in range(self.width)]

        else:
            room_max = str(self.width * self.height)
            print("MAP NOT INITIALIZED: The maximum possible number of rooms with these dimensions is: " + room_max + ". Please increase your grid dimensions or decrease the desired number of rooms.")

    def generate_map(self):

        # Clear map by setting all values to False
        for p in range(0, self.width):
            for q in range(0, self.height):
                self.map_grid[p][q] = False

        # Choose starting cell; approximate center of map
        x = int(self.width/2)
        y = int(self.height/2)

        ## set x and y to a tuple variable like self.start_room = self.map_grid[x][y]
        print((x, y))

        # Flip the value of the cell in self.map_grid from False to something.
        # Loop until desired number of rooms have been populated
        room_count = 0
        while room_count < self.total_rooms:

            # If the cell is still False, provide value
            if not self.map_grid[x][y]:
                if room_count == 0:
                    self.map_grid[x][y] = "Start"
                    room_count += 1
                elif room_count == self.total_rooms - 1:
                    self.map_grid[x][y] = "End"
                    room_count += 1
                else:
                    self.map_grid[x][y] = True
                    room_count += 1

            # Randomly move to a neighbouring cell to populate
            n = x, y+1
            e = x+1, y
            s = x, y-1
            w = x-1, y

            direction = [n, e, s, w]
            next_room = random.randint(0, len(direction) - 1)

            new_room = direction[next_room]
            new_x = new_room[0]
            new_y = new_room[1]

            if new_x < self.width and new_x >= 0:
                if new_y < self.height and new_y >= 0:
                    x = new_x
                    y = new_y
                else:
                    pass # Otherwise pass and try again
            else:
                pass # Otherwise pass and try again

