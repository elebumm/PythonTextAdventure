################################################################################################
#
# Use this as a reference for importing. Instead of "from leaf import *" use:
#
# from leaf import Leaf
#
# IN THIS MODULE:
#
# CLASSES:
#   * Leaf
#
# METHODS:
#
################################################################################################

################################################################################################
#
# USAGE
#
# Leaf is not used by itself.
#
# It is a class inherited by other classes. Leaf objects are contained in Node objects.
# See node.py for more details
#
# EXAMPLES
#
# class ItemPlain(Leaf)
#
# See bottom of page for Leaf METHOD EXAMPLES.
#
################################################################################################

class Leaf(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        
        self.parent = None

    # Attribute getters/setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    # self.parent = None // Modification
    # Helper functions for node_move

    def set_parent(self, parent):
        parent.add_children(self)

    def reset_parent(self):
        if isinstance(self.parent, Node):
            self.parent.remove_children(self)

    def reparent(self, new_parent):
        self.reset_parent()
        self.set_parent(new_parent)

################################################################################################
#
# METHOD EXAMPLES
#
# Uncomment the ## areas to enable an example
# Highlight the region then press Alt + 4 to uncomment
# Alt + 3 to recomment
#
# There is no reason to create a Leaf instance except for demonstration purposes.
#
# Imports for use in examples:

#
################################################################################################

################################################################################################
#
# 1. Creating an instance of Leaf
#
##leaf1 = Leaf("leaf1", "This is leaf1")
#
################################################################################################

################################################################################################
#
# 2. Getting and setting properties
#
##leaf1 = Leaf("leaf1", "This is leaf1")
##print(leaf1.name)
##print(leaf1.description)
##print()
##
##leaf1.name = "new name"
##leaf1.description = "This is still leaf1 but renamed"
##
##print(leaf1.name)
##print(leaf1.description)
#
################################################################################################

################################################################################################
#
# 3. Setting & Resetting object parent. Reparenting objects.
#
##See node.py example 5a and 5b.
#
################################################################################################
