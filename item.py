################################################################################################
#
# Use this as a reference for importing. Instead of "from item import *" use:
#
# from node import ItemContainer, Item, Consumable, KeyItem, Weapon, Armor
#
# IN THIS MODULE:
#
# CLASSES:
#   * ItemContainer (Node)
#
#   * Item (Leaf)
#
#       * Pickup
#           * Consumable (Pickup)
#           * KeyItem (Pickup)
#
#       * Equipment
#           * Weapon (Equipment)
#           * Armor (Equipment)
#
#
#
# METHODS:
#
################################################################################################

################################################################################################
#
# USAGE
#
# Items are interactive, non-living, non-enemy objects that serve a variety of purposes.
#
# Pickups can be split into two categories:
#   * Consumables (single-use items that grant bonuses) that go into Player.inventory
#   * KeyItems (items that lock game progression until acquired) that go into Player.key_items
#
# Consumables can replenish health and other stats, teleport you to certain locations, or be
# combat items that are not weapons (e.g. special grenades, deployable shields).
#
# Consumables may come in different sizes (e.g. repair_kit_small/medium/large that replenish different amounts)
#
# KeyItems have simple existence checks; if you have a certain item in Player.key_items, that
# unlocks access to something.
#
# Equipment is anything that goes into Player.weapon_slots and Player.armor_slots. The amount of
# slots a Player has depends on the class they choose.
#
# Equipment consists of weapons and armour pieces & armour sets.
#
# EXAMPLES
#
# See bottom of page for Item METHOD EXAMPLES.
#
################################################################################################

from node import Node, node_search, node_move
from Leaf import Leaf

class ItemContainer(Node):

    def __init__(self, name, description):
        Node.__init__(self, name description)

    #def on_search(self):

class Item(Leaf):

    def __init__(self, name, description):
        Leaf.__init__(self, name description)

class Consumable(Item):

    def __init__(self, name, description, health_replenish):
        Item.__init__(self, name, description)
        
        self.health_replenish = health_replenish

    def use_item(self, targets, target_all):

        if type(targets) == list:
            for target in targets:
                target.health += self.health_replenish
                # remove from inventory
        

class Weapon(Item):

    def __init__(self, name, description, physical_dmg, tarnish_dmg, overload_dmg):
        Item.__init__(self, name, description)

        self.physical_dmg = physical_dmg
        self.tarnish_dmg = tarnish_dmg
        self.overload_dmg = overload_dmg

class Armor(Item):
    
    def __init__(self, name, description, physical_def, tarnish_def, overload_def):
        Item.__init__(self, name, description)

        self.physical_def = physical_def
        self.tarnish_def = tarnish_def
        self.overload_def = overload_def

