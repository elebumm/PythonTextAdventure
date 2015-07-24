################################################################################################
#
# Use this as a reference for importing. Instead of "from room import *" use:
#
# from room import Room
#
# IN THIS MODULE:
#
# CLASSES:
#   * RoomBase
#
# METHODS:
#
#
################################################################################################

################################################################################################
#
# USAGE
#
# Rooms are Nodes containing most of the interactive gameplay elements like Creatures, Items
# (both pickups and interactive room features), and Events
#
# Node.children = [] is overwritten by Room.children = {'creatures': [], 'pickups': [], 'features': []}
#
# Rooms are themselves contained and organized in Floor objects
# RoomRandom is used in conjunction with FloorRandom to generate procedural Floors.
#
# Rooms are navigated with simple north-south and east-west commands according to the Room's exits
# Room.exits is determined by the game designer or automatically when creating FloorRandom
#
# EXAMPLES
#

#
# See bottom of page for Room METHOD EXAMPLES.
#
################################################################################################

from node import Node, node_search, node_move
from leaf import Leaf
from creature import Creature

class RoomBase(Node):

    def __init__(self, name, description, exits=''):
        Node.__init__(self, name, description)
        self.children = {
            'creatures': [],
            'pickups': [],
            'features': []
        }
        
        self.exits = exits ## perhaps make a 'auto_generate_exits' method
        self.coordinate = None

    # self.children['creatures'] // Modification
    # Re-writes the usual Node add/remove child methods to work with dictionaries
    def add_contents(self, contents, content_category):

        if isinstance(contents, (Node, Leaf)):#Creature, Item, Pickup, Feature)):
            self.children[content_category].append(contents)
            contents.parent = self

        elif isinstance(contents, list):

            for content in contents:
                self.children[content_category].append(content)
                content.parent = self

        else:
            print("DEBUG:", "Could not add contents. Contents must be valid Room contents (Creature, Item).")

    def remove_contents(self, contents, content_category):

        if isinstance(contents, (Node, Leaf)):#Creature, Item, Pickup, Feature)):
            self.children[content_category].remove(contents)
            contents.parent = None

        elif isinstance(contents, list):

            for content in contents:
                self.children[content_category].remove(content)
                content.parent = None

        else:
            print("DEBUG:", "Could not remove contents. Contents must be a Creature or Item.")

    def list_contents(self):

        for content_category in self.children:
            print("DEBUG:", content_category)
            for content in self.children[content_category]:
                print("*", content)

    # self.exits // Modification
    def add_exits(self, exitsAdded):
        for char in exitsAdded:
            if char not in self.exits:
                self.exits += exitsAdded

    def remove_exits(self, exitsRemoved):
        for char in exitsRemove:
            self.exits.replace(char, "")

    def find_exits(self):

        if type(self.coordinate) == tuple:

            self.exits = '' # clear current exits
            
            cx = self.coordinate[0]
            cy = self.coordinate[1]

            try:
                self.parent.floor_matrix[cx][cy+1]
                if isinstance(self.parent.floor_matrix[cx][cy+1], RoomBase):
                    self.exits += "n"
            except IndexError:
                pass

            if cy-1 >= 0:
                try:
                    self.parent.floor_matrix[cx][cy-1]
                    if isinstance(self.parent.floor_matrix[cx][cy-1], RoomBase):
                        self.exits += "s"
                except IndexError:
                    pass
                
            try:
                self.parent.floor_matrix[cx+1][cy]
                if isinstance(self.parent.floor_matrix[cx+1][cy], RoomBase):
                    self.exits += "e"
            except IndexError:
                pass

            if cx-1 >= 0:
                try:
                    self.parent.floor_matrix[cx-1][cy]
                    if isinstance(self.parent.floor_matrix[cx-1][cy], RoomBase):
                        self.exits += "w"
                except IndexError:
                    pass

        else:
            print("DEBUG:", "This room is not part of a Floor does not have exits. Use Floor.add_rooms() to add it to a Floor.")            

    # Eventing/Parsing
    def on_room_enter():
        print(self.name)
        # What happens when the player enters the Room:
        # Description or Name is printed
        # A list of enemies is printed
        # A list of room items is printed
        # A list of interactive features is printed (switches, blocks, buttons)
        pass

class RoomEntrance(RoomBase):

    # Entrances contain the same children['creatures']

    def __init__(self, name, description, exits):
        pass

class RoomRandom(RoomBase):

    pass

##room1 = RoomBase("room1", "This is room1")
##rooma = RoomBase("a", "This is a")
##roomb = RoomBase("b", "This is b")
##roomc = RoomBase("c", "This is c")
##roomd = RoomBase("d", "This is d")


#NEEDS A DETECT EXITS METHOD

################################################################################################
#
# METHOD EXAMPLES
#
# Uncomment the ## areas to enable an example
# Highlight the region then press Alt + 4 to uncomment
# Alt + 3 to recomment
#
# There is no reason to create a Node instance except for demonstration purposes.
#
# Imports for use in examples:


#
################################################################################################

################################################################################################
#
# 1. Creating an instance of Node.
#
##node1 = Node("node1", "This is node1")
# 
################################################################################################
