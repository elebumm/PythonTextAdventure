################################################################################################
# ADVENTURE GAME DOCUMENTATION
################################################################################################

################################################################################################
# TITLE: TBD
#
# CONTRIBUTORS:
# * names here
#
# THEMES: Sci-Fi, Robots, Artificial Intelligence, Military
#
# SETTING:
# * Government-owned military research vessel
# * Filled with all sorts of cognitive and physical-capability tests
# * Timeframe: Linear
#
# PLAYER GOAL:
# * Reach the top-floor testing stage
# * To do this, fight enemies, complete puzzles, on floor-by-floor basis
# * Uncover true ending (reach meta-stability level for AI)
#
# GOALS & FUNCTIONALITY:
# * Random enemy generation
# * Random map generation
# * Node system
#
# PROGRESS:
# [YYYY-MM-DD: bulleted list of details (STATUS)]
#
# 2015-6-28:
#   * Project started
#
# 2015-7-9:
#   * Documentation added (ONGOING)
#   * Integrating node and map systems into engine.py (ALTERNATE FIX)
#       * Instead make modules for each major system (route into engine.py?)
#
#   * Class self parameters/methods fix (Room, Player) (COMPLETE)
#   * Creating a demo for newcomers to understand the current structure (ALTERNATE FIX)
#       * Instead defer demo creation till all systems are meshed together nicely
#
# 2015-7-10
#   * Change introduction sequence to a GameEvent
#   * Basic map generation and viewing (COMPLETE)
#   
# 2015-7-12
#   * Create separate modules for each major system (ONGOING)
#   * Update module importing for new file structure (COMPLETE)
#   * Update documentation.py to reflect new modules(IN PROGRESS)
#
# 2015-7-21
#   * Several updates to core system (node.py & leaf.py, floor.py) (COMPLETED)
#   * Tons of code examples added to modules (ONGOING)
#
#
################################################################################################

################################################################################################
#
# GENERAL INHERITANCE
#
#   * main.py // the file that is run to play the game
#   * engine.py // collates all the engine files below
#   * documentation.py // this file! you're reading it right now
#
#   * gameevent.py
#
#   * node.py
#       * creature.py
#           * player.py
#       * gamemap.py
#       * item.py
#       * room.py
#
################################################################################################

################################################################################################
# USING documentation.py
#
# This is a place for all your documentation and discussion question needs.
#
# Comments are sorted by file. See the Table of Contents Above for CTRL+F search
#
# TEMPLATES - Simply copy the templates below to get started. Try to keep your definitions in
# the same order/location as in the engine.py file for easier lookup.
#
# VOTING FORM - If you have a simple design choice you want to vote on try this:
#
# Yes or no question? Names of voters who say yes | Names of voters who say no
#
# If you have to discuss it, use Slack.
#
################################################################################################

# CLASS DEFINITION
################################################################################################
#
# CLASS NAME:       ClassName
# INHERITS FROM:    Inherited classes
#
# DESCRIPTION: description
# 
# Method definitions go here (see METHOD DEFINITION template)
################################################################################################

################################################################################################
# Examples
#
# CLASS NAME:       Creature
# INHERITS FROM:    Node
#
# DESCRIPTION: The base Creature class for creature entities.
################################################################################################

# Method definitions have two formats: single-line or multi-line

# METHOD DEFINITION //single-line
################################################################################################
#
# method_name(return type): description
#
################################################################################################

# METHOD DEFINITION // multi-line
################################################################################################
#
# METHOD NAME:              method_name
# FULL METHOD NAME:         full_method_name
#
# METHOD SIGNATURE:         method_signature
# FULL METHOD SIGNATURE:    full_method_signature
# 
# RETURN TYPE:              return Class
#
# METHOD DESCRIPTION:       description
#
################################################################################################

################################################################################################
#
# Why FULL? You can write a shorter method name and signature parameters for typical use and
# give a full more descriptive name in the docs.
#
# For example, there is a "print message" method which would have a name: print_message and the
# signature: (speaker, message) but in the actual file you may have the following:
#
# def pm(spk, msg):
#   if spk == "":
#       print(msg)
#   else:
#       print(spk + ": " + msg)
#
################################################################################################

################################################################################################
# Examples
#
# 1. Single Line
#
# bse: Create SpeechEvent objects in bulk and print them out with specified speaker lists,
# message lists and sleep times.
#
# 2. Class-like
#
# METHOD NAME:              bse
# FULL METHOD NAME:         bulk_speech_event
#
# METHOD SIGNATURE:         (speaker_list, message_list, wait_list)
# FULL METHOD SIGNATURE:    (slist, mlist, wlist)
#
# RETURN TYPE:              print statement (of SpeechEvents)
#
# DESCRIPTION: Create Speech Event objects in bulk and print them out with the specified speaker
# lists, message lists and sleep times.
################################################################################################

################################################################################################
#
# Node and Leaf
#
################################################################################################

# CLASS DEFINITION
################################################################################################
#
# CLASS NAME:       Node
# INHERITS FROM:    The base object
#
# DESCRIPTION: A Node is an abstraction for a 'container'. It is something that can contain
# other objects (Leaf objects or other Node objects).
#
# A single nested example is an item (a Leaf) inside a chest (a Node).
#
# You can have multiple levels of nested Leaf/Node objects.
# 
# For example, a Room object may contain Creature nodes (Player, Enemy) or non-living containers
# like chests (another Node) which may itself contain a treasure item (a Leaf) or a backpack (a
# Node object).
#
# A Player can move nodes and leaves around, for example by taking the treasure in the chest or
# looting the body of an enemy.
#
# SEE ALSO: Leaf
#
# STORAGE:
#
##    def listChildren(self):
##        for child in self.children:
##            print (child.description)
##            if isinstance(child,Node):
##                child.listChildren()
#
################################################################################################

# CLASS DEFINITION
################################################################################################
#
# CLASS NAME:       Leaf
# INHERITS FROM:    The base object
#
# DESCRIPTION: A Leaf is an abstraction for any item that can be contained in a Node but cannot
# itself contain a Node.
#
# For example, the Player may carry around items inside its inventory. Those items are Leaf
# objects on the Player.
#
# SEE ALSO: Node
################################################################################################

################################################################################################
# Node and Leaf methods
#
# Functions to find and move the nodes around. Basically everything that can contain something
# like a box with keys or stuff will inherit from Node. Other items like keys will inherit from
# Leaf.
#
# If the player picks up keys from a box, move_node will be used. It'll remove it from the
# box and place it in the player's inventory.
#
# search_node returns an object.
################################################################################################

# METHOD DEFINITION
################################################################################################
#
# METHOD NAME:              
# FULL METHOD NAME:         node_search
#
# METHOD SIGNATURE:         (target, parent)
# FULL METHOD SIGNATURE:    (target_child_object, parent_node_object)
#
# RETURN TYPE:              Node object or print statement (search failure)
#
# METHOD DESCRIPTION: node_search iterates over a parent node (parent) and searches its
# immediate children for the target object (target).
#
# SEE ALSO: node_search_deep
#
# STORAGE:
#
##def search_node(nodename,rootnode):
##    nodefound = False
##    for child in rootnode.children:
##        if child.name == nodename:
##            nodefound = True
##            return child
##        elif isinstance(child,Node):
##            search_node(nodename,child)
##    if nodefound is False:
##        print ("Sorry no such item found.")
#
################################################################################################

# METHOD DEFINITION
################################################################################################
#
# METHOD NAME:              
# FULL METHOD NAME:         node_search_deep
#
# METHOD SIGNATURE:         (target, parent)
# FULL METHOD SIGNATURE:    (target_child_object, parent_node_object)
#
# RETURN TYPE:              Node object or print statement (search failure)
#
# METHOD DESCRIPTION: Same as node_search but also searches the Node object's children for the
# target object (target).
#
# SEE ALSO: node_search
#
################################################################################################

# METHOD DEFINITION
################################################################################################
#
# METHOD NAME:              
# FULL METHOD NAME:         node_move
#
# METHOD SIGNATURE:         (target, destination)
# FULL METHOD SIGNATURE:    (target_object, destination_node)
#
# RETURN TYPE:              None or print statement (move failure)
#
# METHOD DESCRIPTION: Moves target object (target) to a new destination Node (destination).
# target is removed from it's parent's children list and made a child of destination instead.
#
# SEE ALSO: node_search, node_search_deep
#
# STORAGE:
#
##def move_node(obj,destination):
##    if isinstance(destination,(Node,Creature)):
##        parentnode = search_node(obj.parent,rootnode)   ##Always pass the topmost?
##        parentnode.children.remove(obj)
##        destination.addChild(obj)
##    else:
##        print("Sorry. The destination cannot contain anything.")
#
################################################################################################

# CLASS DEFINITION
################################################################################################
#
# CLASS NAME:       Room
# INHERITS FROM:    Node
#
# DESCRIPTION: The Room base class. Defines Room objects to be placed into a Map that the player
# can navigate.
#
# SEE ALSO: Node
#
################################################################################################

# CLASS DEFINITION
################################################################################################
#
# CLASS NAME:       Item
# INHERITS FROM:    Leaf
#
# DESCRIPTION: The Item base class. Defines Item objects that occupy Rooms.
#
# SEE ALSO: Leaf
#
# Planned features:
#
# How to handle ammunition/large quantity items.
# Static/immutable Room features (furniture, interactive buttons, switches)
# Inventory Items
# Equippable Items
# Enemy loot
#
################################################################################################

################################################################################################
# CLASS: Creature
#
# DESCRIPTION: The Creature base class for player and enemies.
#
################################################################################################

################################################################################################
# CLASS: Player
#
# DESCRIPTION: The Player class
#
################################################################################################
