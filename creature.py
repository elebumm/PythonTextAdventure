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

# class Creature(Node):

#     def __init__(self, name, description):
#         Node.__init__(self, name, description)
#         self.creature_type = creature_type
#         self.isAlive = True

class Creature(Node):

    def __init__(self, name, description, creature_type, health, armors):
        Node.__init__(self, name, description)
        self.creature_type = creature_type

        self.health = health

        self.armor = armors[0]
        self.resist_tarnish = armors[1]
        self.resist_environment = armors[2]
    
    def inflict_damage(self, damage):
    	final_damage = damage - self.armor
    	self.health -= final_damage
    	

    def 


# Damage formulas
# final_damage = damage - self.armor
#
#
#
#