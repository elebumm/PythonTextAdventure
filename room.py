################################################################################################
#
# Use this as a reference for importing. Instead of "from room import *" use:
#
# from room import Room
#
# IN THIS MODULE:
#
# CLASSES:
#   * Room
#
# METHODS:
#
#
################################################################################################

from node import Node, Leaf, node_search, node_search_deep, node_move

class Room(Node):

    def __init__(self, name, description, exits):
        Node.__init__(self, name, description)
        self.exits = exits
        self.get_name()

    def get_name(self):
        print("You are in the " + self.name)
        print()

    def set_description(self, description):
        self.description = description
        
    def get_description(self):
        print(self.description)
        print()
        
    def get_exits(self): ## Debug
        print(self.exits)

    def add_exits(self, exitsAdded):
        for char in exitsAdded:
            if char not in self.exits:
                self.exits += exitsAdded

    def remove_exits(self, exitsRemoved):
        for char in exitsRemove:
            self.exits.replace(char, "")

jungle = Room("jungle", "ballasjf", "nsew")
jungle.get_exits()
