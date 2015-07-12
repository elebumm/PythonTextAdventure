################################################################################################
#
# Use this as a reference for importing. Instead of "from node import *" use:
#
# from node import Node, Leaf, node_search, node_search_deep, node_move
#
# IN THIS MODULE:
#
# CLASSES:
#   * Node
#   * Leaf
#
# METHODS:
#   * node_search
#   * node_search_deep
#   * node_move
#
#
################################################################################################

rootnode = None

class Node(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.children= []

    #Name
    def get_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name

    #Description
    def get_description(self):
        print(self.description)

    def set_description(self, description):
        self.description = description

    #Children
    def add_child(self, child):
        child.parent = self.name
        self.children.append(child)

    def remove_child(self, child):
        child.parent = None
        self.children.remove(child)

    def list_children(self): #lists immediate children
        for c in self.children:
            print(c.name)

    def list_children_deep(self):

        for c in self.children:
            print(c.name)
            if isinstance(c, Node):
                c.list_children_deep()

class Leaf(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description

    #Name
    def get_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name

    #Description
    def get_description(self):
        print(self.description)

    def set_description(self, description):
        self.description = description

def node_search(target, parent):
                    
    nodefound = False

    for child in parent.children:
        if child.name == target:
            nodefound = True
            return child

    if nodefound is False:
        print ("Sorry, no such item found.")

def node_search_deep(target, parent):
                    
    nodefound = False
                    
    for child in parent.children:
        if child.name == target:
            nodefound = True
            return child
        elif isinstance(child, Node):
            node_search_deep(target, child)
                    
    if nodefound is False:
        print ("Sorry no such item found.")
                    
def node_move(target, destination):
                    
    if isinstance(destination, (Node, Creature)): ## Later add Container, Room, etc. ##Actually, later remove that stuff. isinstance can check the superclass of destination
        parentnode = target.parent
        parentnode.children.remove(target)
        destination.addChild(target)
    else:
        print("Sorry. The destination cannot contain anything.")
