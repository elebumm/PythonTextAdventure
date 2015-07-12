################################################################################################
#
# Use this as a reference for importing. Instead of "from item import *" use:
#
# from item import ItemNode, ItemLeaf
#
# IN THIS MODULE:
#
# CLASSES:
#   * ItemNode
#   * ItemLeaf
#
# METHODS:
#
#
################################################################################################

from node import Node, Leaf, node_search, node_search_deep, node_move

class ItemNode(Node):

    def __init__(self, name, description):
        Node.__init__(self)

class ItemLeaf(Leaf):
    
    def __init__(self, name, description):
        Leaf.__init__(self, name, description)


#TESTING
#
##key = ItemLeaf("Blue Token", "An opalescent azure chip the size and shape of a coin.\nYou can see a microchip embedded in it.")
##key.get_name()
##key.get_description()
