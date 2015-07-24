################################################################################################
#
# Use this as a reference for importing. Instead of "from floor import *" use:
#
# from floor import FloorBase, Floor, FloorRandom
#
# IN THIS MODULE:
#
# CLASSES:
#   * FloorBase (Node)
#       * Floor (FloorBase)
#       * FloorRandom (FloorBase)
#
# METHODS:
#
################################################################################################

################################################################################################
#
# USAGE
#
# Floors are Node objects that contain Rooms
#
# The goal of the Player is to ascend all the Floors in a game
#
# Floor elevators are unlocked once the Floor goal is complete; Floor.goal_complete = True
# Floor elevators are unlocked by navigating and interacting with that Floor's Rooms
# Floor elevators may be used at any point after unlocking
#
# Floor objects contain Rooms in an organized 2D matrix to simulate a grid-based map
# Floors also provide map visualization
#
# Every Floor possesses an "entrance", the starting Room for that floor
#
# EXAMPLES
#
# Typical usage:
#
##mf_rooms = [] # a list of Room objects
##mf_coordinates = [(0,0), (0,1), (0,2), (0,3), (0,4), # a list of mapping coordinate tuples
##                  (1,0), (1,1), (1,2), (1,3), (1,4)]
##
##munitions_factory = Floor("Munitions", "A factory for producing ammunition", 5, 5, (2, 2)) # plain Floor created
##munitions_factory.add_rooms(mf_rooms, mf_coordinates) # put the Rooms in mf_rooms into Floor.floor_matrix
#
# See bottom of page for FloorBase, Floor, and FloorRandom METHOD EXAMPLES.
#
################################################################################################

import time
import random

from node import Node, node_search, node_move
from room import RoomBase

class FloorBase(Node):

    def __init__(self, name, description, width, height):
        Node.__init__(self, name, description)

        self.width = width
        self.height = height
        self.entrance = None

        self.floor_matrix = [[False] * self.height for row in range(self.width)]
        self.goal_complete = False

    # self.floor_matrix // Modification
    # Room.coordinate // Modification
    # Node.parent & Node.children // Modification & Viewing

    # Map a single Room or list of Rooms to a single coordinate tuple or list of tuples in self.floor_matrix
    def add_rooms(self, rooms, coordinates):

        if isinstance(rooms, RoomBase) and isinstance(coordinates, tuple):
            x = coordinates[0]
            y = coordinates[1]

            try:
                self.floor_matrix[x][y]
            except IndexError:
                print("Coordinate", (x,y), "does not exist on this floor.", rooms.name, "not added")
                return
            
            if self.floor_matrix[x][y] == False:
                Node.add_children(self, rooms)
                rooms.coordinate = (x, y)
                self.floor_matrix[x][y] = rooms
            else:
                print("DEBUG:", "That coordinate already contains a Room:", self.floor_matrix[x][y].name)

        elif type(rooms) == list and type(coordinates) == list and len(rooms) == len(coordinates):

            for r in range(0, len(rooms)):

                x = coordinates[r][0]
                y = coordinates[r][1]

                try:
                    self.floor_matrix[x][y]
                except IndexError:
                    print("Coordinate", (x,y), "does not exist on this floor.", rooms[r].name, "not added")
                    continue

                if self.floor_matrix[x][y] == False:
                    Node.add_children(self, rooms[r])
                    rooms[r].coordinate = (x, y)
                    self.floor_matrix[x][y] = rooms[r]
                else:
                    print("DEBUG:", "That coordinate already contains a Room:", self.floor_matrix[x][y].name)

        else:
            print(
                "DEBUG:",
                "\nCould not add rooms.",
                "\nFirst parameter must be a Room object or list of Rooms.",
                "\nSecond parameter must be an (x,y) tuple or list of tuples.",
                "\nList lengths must match."
            )

    # Remove a single Room or list of Rooms from self.floor_matrix cells
    # Rooms are removed via coordinate tuple references
    def remove_rooms(self, coordinates):

        if isinstance(coordinates, tuple):
            x = coordinates[0]
            y = coordinates[1]

            try:
                self.floor_matrix[x][y]
            except IndexError:
                print("Coordinate", (x,y), "does not exist on this floor. There is nothing to remove.")
                return

            Node.remove_children(self, self.floor_matrix[x][y])
            self.floor_matrix[x][y].coordinate = None
            self.floor_matrix[x][y] = False

        elif type(coordinates) == list:

            for c in range(0, len(coordinates)):

                x = coordinates[c][0]
                y = coordinates[c][1]

                try:
                    self.floor_matrix[x][y]
                except IndexError:
                    print("Coordinate", (x,y), "does not exist on this floor. There is nothing to remove.")
                    continue

                Node.remove_children(self, self.floor_matrix[x][y])
                self.floor_matrix[x][y].coordinate = None
                self.floor_matrix[x][y] = False

    def list_rooms(self):
        Node.list_children(self)

    # self.entrance // Modification

    def set_entrance(self, coordinate):

        try:
            self.floor_matrix[coordinate[0]][coordinate[1]]
        except IndexError:
            print("DEBUG:", "The cell at coordinate", (coordinate[0], coordinate[1]), "does not exist. Entrance not set.")
            return
                  
        self.entrance = coordinate

    # self.goal_complete // Modification

    def set_goal_complete(self, completion):

        self.goal_complete = True

##        if completion == True or completion == False:
##            self.goal_complete = completion
##        else:
##            print("DEBUG:", "goal_complete must be set to True or False")

    # self.floor_matrix // Correction, map visualization

    def correct_matrix_orientation(self): # Rotate matrix 90 degrees counterclockwise.

        floor_matrix = self.floor_matrix # floor_matrix is useful for everything except viewing
        viewing_matrix = [] # thus we need a viewing matrix that is simply a rotated floor_matrix

        #frow/fcolumn = floor_matrix row/column
        #vrow = viewing_matrix row - the map is printed row by row

        for frow in range(0, self.height):

            vrow = []

            for fcolumn in range(0, self.width):
                vrow.append(floor_matrix[fcolumn][frow])

            viewing_matrix.append(vrow)

        viewing_matrix = list(reversed(viewing_matrix))

        self.viewing_matrix = viewing_matrix # new attribute generated
        
    def view_map(self, room = "#", empty = u"\u25A1", border = u"\u25A0"):

        self.correct_matrix_orientation() # ensure self.viewing_matrix exists

        # top border
        for i in range(0, self.height + 2):
            print(border, end = " ")
        print()

        for j in range(0, self.width):

            # left border
            print(border, end = " ")

            for i in range (0, self.height):

                if self.viewing_matrix[j][i] == "Start":
                    print("S", end = " ")
                elif self.viewing_matrix[j][i] == "End":
                    print("E", end = " ")
                elif isinstance(self.viewing_matrix[j][i], RoomBase):
                    print("R", end = " ")
                elif self.viewing_matrix[j][i]:
                    print(room, end = " ")
                else:
                    print(empty, end = " ")

            # right border
            print(border)

        # bottom border
        for i in range (0, self.height + 2):
            print(border, end = " ")
        print("\n")

class Floor(FloorBase):

    def __init__(self, name, description, width, height, entrance):
        FloorBase.__init__(self, name, description, width, height)
        self.set_entrance(entrance)

class FloorRandom(FloorBase):

    def __init__(self, name, description, width, height, number_of_cells = 0):
        FloorBase.__init__(self, name, description, width, height)
        self.set_number_of_cells(number_of_cells)
        
        self.regenerate_floor_matrix()

    def set_number_of_cells(self, number_of_cells):

        if number_of_cells <= (self.width * self.height):
            self.number_of_cells = number_of_cells
        elif number_of_cells > (self.width * self.height):
            self.number_of_cells = self.width * self.height
            print("DEBUG:", "That is too many cells. number_of_cells set to maximum amount instead. number_of_cells:", self.width * self.height)
        else:
            print("DEBUG:", "number_of_cells not set. Please provide a valid integer.")

    def regenerate_floor_matrix(self):

        # Works by choosing a starting cell coordinate and inserting a Room at that self.floor_matrix index
        # Then randomly chooses a next_cell and inserts a Room there
        # At the moment no Room is actually inserted but the value is changed from False to something else

        # Clears previous self.floor_matrix by setting all cells to False
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.floor_matrix[x][y] = False

        # Starting (x, y) coordinate (approximate center)
        x = int(self.width/2)
        y = int(self.height/2)

        # Fill cells until the desired number_of_cells is reached
        number_of_cells_filled = 0
        while number_of_cells_filled < self.number_of_cells:

            if not self.floor_matrix[x][y]:

                if number_of_cells_filled == 0:
                    self.floor_matrix[x][y] = "Start"
                    self.set_entrance((x,y))
                    
                    number_of_cells_filled += 1

                elif number_of_cells_filled == self.number_of_cells - 1:
                    self.floor_matrix[x][y] = "End"
                    
                    number_of_cells_filled += 1

                else:
                    #self.floor_matrix[x][y] = RoomBase("Room Name", "I am a generic room") #True
                    self.add_rooms(RoomBase("Room Name", "I am a generic room"), (x,y))
                    
                    number_of_cells_filled += 1

            # Randomly choose next_cell
            north = x, y+1
            south = x, y-1
            east = x+1, y
            west = x-1, y

            directions = [north, south, east, west]
            next_direction = random.randint(0, len(directions) - 1)

            next_cell = directions[next_direction]
            next_x = next_cell[0]
            next_y = next_cell[1]

            # Is next_cell within the bounds of the map?
            if next_x < self.width and next_x >= 0:
                if next_y < self.height and next_y >= 0:
                    x = next_x
                    y = next_y
                else:
                    pass # If not, pass and retry
            else:
                pass # If not, pass and retry

    def fill_floor_matrix():
        pass

    def regenerate_room_exits(self):

        for x in range(0,self.width):
            for y in range(0,self.height):
                if isinstance(self.floor_matrix[x][y], RoomBase):
                    self.floor_matrix[x][y].find_exits()
                    print("The exits at", x, y, "are", self.floor_matrix[x][y].exits)
                #else:
                    #print('Cell', x, y, 'is not a Room')

################################################################################################
#
# METHOD EXAMPLES
#
# Uncomment the ## areas to enable an example
# Highlight the region then press Alt + 4 to uncomment
# Alt + 3 to recomment
#
# You should always use FloorBase subclasses, Floor, FloorRandom and so on when creating a floor
#
################################################################################################

################################################################################################
#
# 1. Creating an instance of Floor.
#
##floor1 = Floor("floor1", "Ground level floor", 5, 5, (2,2))
# 
################################################################################################

################################################################################################
#
# 2a. Adding/Removing (mapping) Rooms to Floor.floor_matrix
#
#
### You need a list of Room objects (see room.py for more details) to child to a Floor object
##room1 = Room("room1", "I am the first room", "n")
##room2 = Room("room2", "This is room2", "ns")
##room3 = Room("room3", "room3 is me", "s")
##
##f1_rooms = [room1, room2, room3] # Rooms are collected into a single list
##f1_coords = [(0,0), (0,1), (2,2)]# tuple indices will match f1_rooms' indices; room1 maps to (0,0), room3 maps to (2,2)
##
### Floor methods start here
##floor1 = Floor("floor1", "Ground level floor", 5, 5, (0,1))
##
##for row in floor1.floor_matrix: # Returns False matrix
##    print(row)
##print(floor1.children) # Returns empty list
##print()
##
##print(room1.parent, room2.parent, room3.parent) # Returns None
##print()
##
##floor1.add_rooms(f1_rooms, f1_coords) # alters contents of Floor.floor_matrix and also childs the Rooms to the Floor
##
##for row in floor1.floor_matrix: # Returns matrix with Room objects in place of False
##    print(row)
##print(floor1.children) # Returns list of the 3 Room objects
##print()
##
##print(room1.parent.name, room2.parent.name, room3.parent.name) # Returns floor1
##print()
##
### IMPORTANT! Notice that the floor_matrix is rotated 90 degrees clockwise relative to a Cartesian coordinate system
###
### In a Cartesian plane, if (0,0) is the bottom left corner then (0,1) would be a single point ABOVE that
### Notice however that the Room objects at (0,0) and (0,1) are not at the bottom-left of the matrix
##
### Thus, the RIGHTMOST COLUMN of floor_matrix would be the TOP ROW of the actual map
### Hence, the necessity of correct_matrix_orientation() and view_map() as proper visualization tools
##
##floor1.remove_rooms((0,0)) # Remove the room at coordinate (0,0) and also remove it from children
##
##for row in floor1.floor_matrix: # The object at index (0,0) is gone
##    print(row)
##print(floor1.children) # Returns only 2 Room objects
##print()
##
##print(room1.parent, room2.parent.name, room3.parent.name) # room1 parent has reverted to None
##print()
#
# 2b. Viewing Floor.viewing_matrix
#
##floor1.view_map() # returns a unicode map of Floor.viewing_matrix
##
###view_map() calls Floor.correct_matrix_orienation to ensure Floor.viewing_matrix exists
###Unlike Floor.floor_matrix, this is oriented properly
###The rooms at (0,1) and (2,2) are where you would expect them to be in a Cartesian plane.
#
################################################################################################

################################################################################################
#
# 3. Using FloorRandom and regenerating floor matricess
#
#randfloor = FloorRandom("Random Floor", "I am a random floor", 20, 20, 196)
# This creates a Floor.floor_matrix with total area of 400 but only 196 filled cells
#randfloor.view_map() # Returns unicode Floor.viewing_matrix; S is the start/entrance. E is the endpoint

randfloor2 = FloorRandom("Random Floor: Electric Boogaloo", "This is randfloor2", 10, 10, 12)
randfloor2.view_map() # Notice only 12 Rooms are populated
"""
randfloor2.set_number_of_cells(88) # Overwrite the original number_of_cells (12) at Floor creation
randfloor2.regenerate_floor_matrix()
randfloor2.view_map() # The matrix is now populated with 88 Rooms
"""
# IMPORTANT! No Rooms are actually added yet since the RoomRandom class needs work
#
################################################################################################
