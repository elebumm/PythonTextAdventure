################################################################################################
#
# Use this as a reference for importing. Instead of "from gameevent import *" use:
#
# from gameparse import parse_movement, update_floor, update_room
#
# IN THIS MODULE:
#
# CLASSES:
#
# METHODS:
#   * parse_movement
#   * update_floor
#	* update_room
#
################################################################################################

# class GameParse():

#     def someMethod(self):
#         return 3

# Simplify entrance and exit. No exit room; you can ascend any time you like
# Entrance is still necessary as starting point

def parse_movement(action, floor_list, floor_index, room_matrix, room_position):

    if action.lower().strip() == "floor complete":
        floor_list[floor_index[0]].set_goal_status(True)

    update_floor(action, floor_list, floor_index, room_position)
    update_room(action, room_matrix, room_position)

def update_floor(action, floor_list, floor_index, room_position):

    current_floor = floor_list[floor_index[0]]

    #print("Goal status:", current_floor.get_goal_status())

    if action.lower().strip() == "ascend" or action.lower().strip() == "elevator":
        if current_floor.get_goal_status():
            floor_index[0] += 1
            #print(floor_index[0])
            new_floor = floor_list[floor_index[0]]
            room_position[0] = new_floor.entrance_coordinate[0]
            room_position[1] = new_floor.entrance_coordinate[1]
        else:
            print("The elevator is locked")

def update_room(action, room_matrix, room_position):

    room_exits = room_matrix[room_position[0]][room_position[1]].get_exits()

    if action.lower().strip() == "north" or action.lower().strip() == "n":
        if "n" in room_exits:
            room_position[1] += 1
            print("You head north")
        else:
            print("You cannot pass north")

        return

    elif action.lower().strip() == "south" or action.lower().strip() == "s":
        if "s" in room_exits:
            room_position[1] -= 1
            print("You head south")
        else:
            print("You cannot pass south")

        return

    elif action.lower().strip() == "east" or action.lower().strip() == "e":
        if "e" in room_exits:
            room_position[0] += 1
            print("You head east")
        else:
            print("You cannot pass east")

        return

    elif action.lower().strip() == "west" or action.lower().strip() == "w":
        if "w" in room_exits:
            room_position[0] -= 1
            print("You head west")
        else:
            print("You cannot pass west")

        return