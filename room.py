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
        
    def get_exits(self): ## Debug
        print(self.exits)

    def add_exits(self, exitsAdded):
        for char in exitsAdded:
            if char not in self.exits:
                self.exits += exitsAdded

    def remove_exits(self, exitsRemoved):
        for char in exitsRemove:
            self.exits.replace(char, "")

# TESTING
# jungle = Room("jungle", "baller", "nsew")
# jungle.get_exits()
