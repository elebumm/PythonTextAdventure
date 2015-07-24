#from creature import CreatureBaes
#from player import Player
from node import Node, node_search, node_move
from floor import FloorBase, Floor, FloorRandom
from room import RoomBase
#from item import ItemBase, Pickup, Feature, etc.

room1 = RoomBase("Room1", "This is room1")
room2 = RoomBase("Room2", "This is room2")
room3 = RoomBase("Room3", "This is room3")
room4 = RoomBase("Room4", "This is room4")
room5 = RoomBase("Room5", "This is room5")
room6 = RoomBase("Room6", "This is room6")

floor1 = Floor("floor1", "I am floor1", 3, 3, (0,0))

rooms = [room1, room2, room3, room4, room5, room6]
rc = [(1,1), (1,2), (1,0), (0,1), (2,1), (0,2)]

floor1.add_rooms(rooms, rc)

print(room1.exits)
print(room2.exits)
print(room3.exits)
print(room4.exits)
print(room5.exits)
print(room6.exits)

room1.find_exits() #nsew
room2.find_exits() #sw
room3.find_exits() #n
room4.find_exits() #ne
room5.find_exits() #w
room6.find_exits() #se

print(room1.exits)
print(room2.exits)
print(room3.exits)
print(room4.exits)
print(room5.exits)
print(room6.exits)


################################################################################################
# CREATING THE GAME
#
# This details, in a general sense, how you would use the above classes and in what order.
# Remember that the game operates on a Node & Leaf system; objects inside objects.
#
################################################################################################


################################################################################################
#
# 1. Create the lowest level objects first: Leaf > ItemBase > Item > Pickup > Consumable
#
# Leaf objects are lowest level because they cannot contain other objects.
# Leaf objects can only sit inside Node objects so in RPG terms, you can think of any Leaf as
# being some inventory consumable, equipment, or key item.
#
# EXAMPLES
#
# scrap_metal = Pickup("scrap metal", "A refined sheet of metal used for armor repair")
#
# upgrade_unit_memory = Consumable(...)
# upgrade_unit_armor = Consumable(...)
#
# red_keycard = Pickup(...)
#
#
################################################################################################

################################################################################################
#
# 2. Since all gameplay takes place "inside" Room objects, we need to fill them with all the gameplay elements.
#
# Rooms can contain the bare Pickups and Consumables seen in Phase 1 (for example, ammunition
# on the floor of the Room)
#
# However, these Pickups can move to other Node objects contained in the Room itself
# For example, an item held by a Creature or Container inside a Room.
#
# We have to create these Node objects first.
#
# EXAMPLES
#
# 2a. Creatures
#
# robot_unicorn = Creature(...)
# fifty_cal_turret = Creature(...)
# mining_drill = Creature(...)
#
# And you can populate the Creatures' inventories.
#
# robot_unicorn.add_children(scrap_metal)
#
# 2b. Containers
#
# backpack = Container(...)
# backpack.add_children(...)
#
# This step is likely going to contain the largest amount of code
#
################################################################################################

################################################################################################
#
# 3a. Create Room objects. Fill them with the objects created in Phase 1 and 2.
#
# lobby = Room(...)
# lobby.add_contents(list_of_creatures, 'creatures')
#
# 3b. Create a randomized room.
#
# jungle_brush = RoomRandom(list_of_creatures, list_of_pickups, list_of_features)
# 
################################################################################################

################################################################################################
#
# 4a. Create Floor objects and map rooms to the floor_matrix
#
# munitions_factory = Floor(...)
# munitions_factory.add_rooms(list_of_Room_objects, list_of_tuple_coordinates)
#
# munitions_factory.set_entrance((x, y)) # Set the starting Room
#
# 4b. Create FloorRandom
#
# no example yet
#
################################################################################################

################################################################################################
#
# 5. Collect the Floors which contain Rooms which contain other Nodes (which contain other Nodes
# and Leafs) and Leafs into a list for the parser to use
#
# floor_list = [floor objects go here]
# floor_index = 0 # floor_list should be ordered according to design of game
# current_floor = floor_list[floor_index]
#
# room_matrix = current_floor.floor_matrix
# room_coordinate = current_floor.entrance
# current_room = room_matrix[room_coordinate[0]][room_coordinate[1]]
#
################################################################################################
