import time
import random

# GLOBALS

help = "Type 'help' for all available options."
error = "Command not recognized"
#spacer just puts the line just for easier readability. Just use print(spacer)
spacer = "-----------------------------------------------------------------------------------------------"

visited = {'medical_bay': False}
x = 1
y = 1
room = (x, y)
key1 = 0
key2 = 0
dooropen = 0

inprogress = "Nothing happens 'cause I didn't code it in yet"

ending = 0

################################################################################################ There are 96 # symbols per spacer
# You should know upfront that I write a lot
# It's how I best communicate
# Please write however you are comfortable
#
# There's a lot of writing here because of the game system considerations
# that I want to run by you. It's also useful to document for future team members.
#
# Probably best just to start and see where it goes
#
################################################################################################

################################################################################################
# TITLE: TBD
#
# THEME: Sci-Fi Thriller
#
# SETTING:
# * Derelict Ship or Ship with Skeleton Crew like in Alien(s)?
# * Ship is government-owned. A scientific research vessel
# * Timeframe: In medias res or at the genesis?
# * Shenanigans occur; juxtapose serious situation with humour
# * A whale is involved somehow, even if only tangentially
#
# GOALS & FUNCTIONALITY:
# * This is important to set becase we could do this forever if we get good at it
# * As vague or specific as you like
#
# Examples:
# * A system where enemy that stalks you can moves per ratio of your movement
# * Random success events
# * Time limit
#
# PROGRESS:
# [YYYY-MM-DD: bulleted list of details]
# 2015-6-28:
#   * Project started
#
#
#
#
#
#
#
################################################################################################

################################################################################################
# SIGNATURE: direction_check(exits, action)
# 
# DESCRIPTION: A basic check for character movement.
#
# Movement is parsed in two steps:
# 1. Was a movement command issued?
# 2. Is that movement available in the "exits" string?
#
# Movement is parsed last (in the else statement) since "exits" may vary with other code.
# For example, adding exits depending on inventory:
#
# if hasKey:
#   exits += "w"
#
# CONSIDERATIONS:
# * Generic negative message - perhaps add rejection field taken as array so signature is:
#
# direction_check(exits, action, customMessages):
#
#   if action.lower() ... etc:
#
#   else:
#       print(customMessages[0])
#
# Additional parameters may be useful in other cases.
#
# * Vertical movement - "You see a hole in the ceiling", action = "climb"
#   or even more simply "You see a set of stairs".
#
# * Trap rooms where exits = ""
#
################################################################################################

def direction_check(exits, action):

    if action.lower() == "north" or action.lower() == "n":
        if "n" in exits:
            y += 1
            room = (x, y)
    #else: // Custom failure message

    elif action.lower() == "south" or action.lower() == "s":
        if "s" in exits:
            y -= 1
            room = (x, y)

    elif action.lower() == "east" or action.lower() == "e":
        if "e" in exits:
            x += 1
            room = (x, y)

    elif action.lower() == "west" or action.lower() == "w":
        if "w" in exits:
            x -= 1
            room = (x, y)

    else: # Generic failure message
        print("You cannot go that way.")
        

################################################################################################
# SIGNATURE: room_name()
#
# DESCRIPTION: Contains the parser for player actions in that room but also properties
# for that room e.g. visited = true, exits = "ne"
#
################################################################################################

def introduction():
    print('Welcome to Text Adventure by Lewis Menelaws')
    print("If you need help throughout the game, just type HELP for all available actions")
    print("On that note. Let's get started")
    #time.sleep(6)

def initialize_room(room_name, room_description):
    print(spacer)
    print(spacer)
    print()
    print(room_description)
    visited[room_name] = True
    #maybe pass in some more values


def medical_bay():

    room_name = 'medical_bay'
    exits= "n"

    #Have different messages if you've entered a room before
    initial = ("You awake in a comfy bed to the ministrations of an auto-nurse and a bright glare.\n"
            "White linens. White walls. White lights.\n"
            "There is a white door at the north end of the room.\n"
            "You are in the medical bay of the /OBLIVIOUS/.\n"
            "You wave away the medical robot and climb out of bed.")

    subsequent = ("A janitor's nightmare.")
    
    if visited[room_name]:
        initialize_room(room_name, initial)
        #working out some flaws here
    else:
        print(subsequent)

    action = input("> ")

    if action.lower() == "hello":
        print("Hello back")
    else:
        print(inprogress)

    
    


################################################################################################
# SIGNATURE: game_loop()
#
# DESCRIPTION: A simple while loop that checks what room you're in.
#
# Game runs on a map system. While the game loop is in play, it constantly checks the "room"
# variable. "room" changes depending on player actions and different scenarios are loaded.
#
# Game start variables are initialized at the top like inventory and starting room.
# EDIT: Variables have been moved to a global scope above. Needs testing
#
# CONSIDERATIONS:
#
# * Probably should use a dictionary for the inventory.
# I like to map 0 = item undiscovered, 1 = item in inventory, 2 = item consumed
#
# inventory = {
#   'key1': 0,
#   'key2': 0,
#   'frying pan': 0,
#   'pocket knife': 1
# }
#
# * Consider initializing player variables
#
# appearance = "camouflaged" // maybe for a stealth segment
# health = 100 // if you want health
#
#
################################################################################################

def game_loop():
    

    introduction()
    
    while ending == 0:
        
        if room == (1, 1):
            medical_bay()
            

game_loop()
