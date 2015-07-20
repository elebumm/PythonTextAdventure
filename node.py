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

#rootnode = None

class Node(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.children= []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    #Children
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def remove_child(self, child):
        child.parent = None
        self.children.remove(child)

    def list_children(self): #lists immediate children
        for child in self.children:
            print(child.name)

    def list_children_deep(self):

        for child in self.children:
            print(child.name)
            if isinstance(child, Node):
                child.list_children_deep()

class Leaf(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

def node_search(target_string, parent):
                    
    nodefound = False

    for child in parent.children:
        if child.name == target_string:
            nodefound = True
            return child

    if nodefound is False:
        print ("Sorry, no such item found.")

def node_search_deep(target_string, parent):
                    
    nodefound = False
                    
    for child in parent.children:
        if child.name == target_string:
            nodefound = True
            return child
        elif isinstance(child, Node):
            node_search_deep(target_string, child)
                    
    if nodefound is False:
        print ("Sorry no such item found.")
                    
def node_move(target, destination):
                    
    if isinstance(destination, Node): ## Later add Container, Room, etc. ##Actually, later remove that stuff. isinstance can check the superclass of destination
        parentnode = target.parent
        parentnode.children.remove(target)
        destination.add_child(target)
    else:
        print("Sorry. The destination cannot contain anything.")

# exampleNode = Node("aname", "desc duh")
# anotherNode = Node("another name", "some description")
# leaf1 = Leaf("leaf1", "a leaf")
# leaf2 = Leaf("leaf2", "another leaf")
# exampleNode.add_child(leaf1)
# exampleNode.add_child(leaf2)