################################################################################################
#
# Use this as a reference for importing. Instead of "from creature import *" use:
#
# from creature import Creature
#
# IN THIS MODULE:
#
# CLASSES:
#   * Creature
#
# METHODS:
#
#
################################################################################################

from node import Node, Leaf, node_search, node_search_deep, node_move

class Creature(Node):

    def __init__(self, name, description, creature_type):
        Node.__init__(self, name, description)
        self.creature_type = creature_type
        self.isAlive = True
