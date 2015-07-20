import time
from node import Node, Leaf, node_search, node_search_deep, node_move
from room import Room
from gamemap import GameMap, Floor, RandomFloor
from gameevent import GameEvent, SpeechEvent, bulk_speech_event
from gameparse import parse_movement, update_floor, update_room

# This example uses manual map creation

# Room creation
militia_tent = Room("Rebel Tent", "A canvas shelter.", "n")
militia_truck = Room("Rebel Truck", "An all-terrain military vehicle.", "ns")
militia_messhall = Room("Rebel Mess Hall", "A place for eating.", "ns")
militia_camp = Room("Rebel Camp", "A fire warms the vicinity.", "s")

dank_den = Room("Dank Den", "A wet warren", "n")
dank_canopy = Room("The Canopy", "Lazing around in the treetops", "ns")
dank_path = Room("Jungle Path", "Watch your step", "ns")
dank_riverbed = Room("Jungle Riverbed 1", "Beware running water", "s")

# Rooms are collected into a list
# These Rooms are mapped 1:1 to their desired coordinates
forestRooms = [militia_tent, militia_truck, militia_messhall, militia_camp]
forestCoords = [(1, 1), (1, 2), (1, 3), (1, 4)]

jungleRooms = [dank_den, dank_canopy, dank_path, dank_riverbed]
jungleCoords = [(1, 1), (1, 2), (1, 3), (1, 4)]

# Floor(GameMap) creation
forest = Floor("A forest, duh", "Arboreal everything", 5, 5)

# map_rooms_to_cell takes the lists above and stores
# the Rooms (forestRooms) into the desired map_grid indices (forestCoords)
forest.map_rooms_to_cell(forestRooms, forestCoords)

# same thing for another Floor
jungle = Floor("A jungle!", "Tarzan, jungle man", 12, 12)
jungle.map_rooms_to_cell(jungleRooms, jungleCoords)
jungle.set_entrance([1, 4])
#print(jungle.get_entrance())

# These are globals that are used to decide what floor & room you are in
floors = [forest, jungle] # list of Floor objects
floor_index = [0] # starting Floor object
current_floor = floors[floor_index[0]] # The current floor object itself

rooms = current_floor.map_grid # The Room matrix is just the floor's map_grid
room_position = [1, 1]
current_room = rooms[room_position[0]][room_position[1]]

def load_room(floor_list, floor_index, room_position):
	current_floor = floor_list[floor_index[0]]
	rooms = current_floor.map_grid
	rooms[room_position[0]][room_position[1]].onload()

ending = 0

while ending == 0:
	load_room(floors, floor_index, room_position)
	action = input("> ")
	#current_room, room_x, room_y = update_room(action, rooms, room_x, room_y)
	parse_movement(action, floors, floor_index, rooms, room_position)

