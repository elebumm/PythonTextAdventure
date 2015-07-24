################################################################################################
#
# Use this as a reference for importing. Instead of "from node import *" use:
#
# from node import Node, node_search, node_move
#
# IN THIS MODULE:
#
# CLASSES:
#   * Node
#
# METHODS:
#   * node_search
#   * node_move
#
################################################################################################

################################################################################################
#
# USAGE
#
# Node is not used by itself.
#
# It is a class inherited by other classes to simulate container-like objects, anything with a
# parent-child relationship.
#
# See those classes for individual use cases
#
# EXAMPLES
#
# class Floor(Node)
# class Room(Node)
# class Creature(Node)
#
# See bottom of page for Node METHOD EXAMPLES.
#
################################################################################################

class Node(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        
        self.parent = None
        self.children = []

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

    def description(self, description):
        self._description = description

    # self.children = [] // Modification, Viewing
    def add_children(self, children):

        if isinstance(children, (Node, Leaf)):
            self.children.append(children)
            children.parent = self # give child reference to its parent Node object

        elif isinstance(children, list):

            for child in children:
                self.children.append(child)
                child.parent = self # give child reference to its parent Node object

        else:
            print("DEBUG:", "Could not add children. Children must be a Node/Leaf or a list of Node/Leaf.")

    def remove_children(self, children):

        if isinstance(children, (Node, Leaf)):
            self.children.remove(children)
            children.parent = None

        elif isinstance(children, list):

            for child in children:
                self.children.remove(child)
                child.parent = None

        else:
            print("DEBUG:", "Could not remove children. Children must be a Node/Leaf or a list of Node/Leaf.")

    def list_children(self):

        for child in self.children:
            #print("NAME: " + child.name + ", TYPE: " + str(type(child)))
            print(child.name, child)

    def view_contents(self):

        for child in self.children:
            print(child.name, child)
            if isinstance(child, Node):
                child.view_contents()

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
        
def node_search(target, parent): # Search a Node object for target object or by target object name (a string)

    target_found = False

    if type(target) == str:

        for child in parent.children:
            if child.name == target:
                target_found = True
                return child

        if target_found == False:
            print("Target not found in this node.")

    elif isinstance(target, (Node, Leaf)):

        for child in parent.children:
            if child == target:
                target_found = True
                return child

        if target_found == False:
            print("Target not found in this node.")

def node_move(target, destination): # Move the target object to the destination Node

    if isinstance(destination, Node):
        target.reparent(destination)

    else:
        print("The destination is not a Node object.")

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

from leaf import Leaf

#
################################################################################################

################################################################################################
#
# 1. Creating an instance of Node.
#
##node1 = Node("node1", "This is node1")
# 
################################################################################################

################################################################################################
#
# 2. Getting and setting properties
#
##node1 = Node("node1", "This is node1")
##print(node1.name)
##print(node1.description)
##print()
##
##node1.name = "new name"
##node1.description = "This is still node1 but renamed"
##
##print(node1.name)
##print(node1.description)
#
################################################################################################

################################################################################################
#
# 3. Adding/Removing a single child.
#
# 3 ways to view children: print(node1.children), node1.list_children(), node1.view_contents()
#
##node1 = Node("node1", "This is node1")
##leaf1 = Leaf("leaf1", "This is leaf1")
##
##node1.list_children() # Returns nothing
##print()
##
##node1.add_children(leaf1) # Add a child
##
##node1.list_children() # Returns single leaf child
##print()
##
##node1.remove_children(leaf1) # Remove child
##
##node1.list_children() # Returns nothing again
#
################################################################################################

################################################################################################
#
# 4. Adding/Removing multiple children.
#
##node1 = Node("node1", "This is node1")
##leaf1 = Leaf("leaf1", "This is leaf1")
##leaf2 = Leaf("leaf2", "Hello, I'm leaf2")
##leaf3 = Leaf("leaf3", "leaf3, that's me")
##
##node1.list_children() # Returns nothing
##print()
##
##node1.add_children([leaf1, leaf2, leaf3]) # Add multiple children by passing a list
##
##node1.list_children() # Returns Leaf objects 1 through 3
##print()
##
##node1.remove_children([leaf1, leaf3]) # Remove multiple children by passing a list
##
##node1.list_children() # Only leaf2 remains
#
#################################################################################################

#################################################################################################
#
# 5a. Setting & Resetting object parent. Reparenting objects.
#
# this_node.set_parent(new_parent) IS EQUIVALENT TO new_parent.add_children(this_node)
# this_node.reset_parent() IS EQUIVALENT TO new_parent.remove_children(this_node)
#
##node1 = Node("node1", "This is node1")
##node2 = Node("node2", "I am node2")
##node3 = Node("node3", "The third node")
##leaf1 = Leaf("leaf1", "This is leaf1")
##
##leaf1.set_parent(node1) # Set leaf1's parent to node1. Same as making leaf1 a child of node1
##
##print(node1.children) # Returns leaf1 object
##print(node2.children) # Returns empty list
##print(leaf1.parent.name) # Returns node1, its parent
##print()
##
##leaf1.reparent(node2) # Change leaf1's parent from node1 to node2
##
##print(node1.children) # Returns empty list
##print(node2.children) # Returns leaf1 object
##print(leaf1.parent.name) # Returns node2, its new parent
##print()
##
##leaf1.reset_parent() # Set leaf1's parent to None. Same as removing leaf1 from its parent
##
##print(node1.children) # Returns empty list
##print(node2.children) # Also an empty list
##print(leaf1.parent) # Returns None
##print()
#
# 5b. view_contents() and parenting continued (you have to uncomment both 5a and 5b)
#
### Chain of parents
##node2.set_parent(node1)
##node3.set_parent(node2)
##leaf1.set_parent(node3)
##
##print(node1.children) # Returns node2
##node1.view_contents() # View children (node2) and children of children (node2, node3 and leaf1)
##print()
##
##node2.reset_parent() # Remove node2 from node1's children
##
##print(node1.children) # Returns empty list
##node1.view_contents() # View nothing
#
#################################################################################################

#################################################################################################
#
# 6. node_search by object & node_search by name
#
##node1 = Node("node1", "This is node1")
##
##leaf1 = Leaf("alice", "This is leaf1")
##leaf2 = Leaf("bob", "Hello, I'm leaf 2")
##leaf3 = Leaf("charlie", "leaf3, that's me")
##
##node1.add_children([leaf1, leaf2, leaf3])
##
##print(node_search(leaf1, node1)) # Search by object returns leaf1 object
##print()
##
##print(node_search("alice", node1)) # Search by name also returns leaf1 object
##print()
##
##node_search("delta", node1) # Not found
##print()
##
##print(node_search("bob", node1)) # Returns leaf2 object
##print(node_search(leaf2, node1).description) # Returns leaf2 description
##print(node_search("charlie", node1).name) # Returns leaf3 name
#
#################################################################################################

#################################################################################################
#
# 7. node_move
#
# node_move is a wrapper for the reparent method
# this_node.reparent(new_parent) IS EQUIVALENT TO node_move(this_node, new_parent)
#
##node1 = Node("node1", "This is node1")
##node2 = Node("node2", "I am node2")
##node3 = Node("node3", "The third node")
##
##node1.add_children(node3)
##
##print(node1.children) # Returns node3 object
##print(node2.children) # Returns empty list
##print()
##
##node_move(node3, node2) # move node3 from node1 to node2. Same as calling node3.reparent(node2)
##
##print(node1.children) # Returns empty list
##print(node2.children) # Returns node3 object
##print()
##
##node_move(node2, node1) # node3 is inside node2. node2 is inside node1
##
##print(node1.children) # Returns node2
##print(node2.children) # Still the node3 object
#
#################################################################################################
