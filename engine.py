import time

## Usually, get_functions() are for debugging.

################################################################################################
# Character Creation
################################################################################################

class Player(object):

    name = ""
    abilities = {'rustic': 0, 'milquetoast': 1, 'charlie': 2, 'apex': 3}
    ability = 0
    # lots of property ideas
    description = ""
    visibility = "visible"

    def __init__(self):
        print("Player created")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

    def set_ability(self, abilities_key):
        self.ability = self.abilities[abilities_key]
        print(self.ability)

    def get_ability(self):
        return self.ability

def calculate_ability(answer1, answer2):
    ## going to mix these up later
    if answer1 and answer2:
        return 'apex'
    elif answer1 and not answer2:
        return 'charlie'
    elif not answer1 and answer2:
        return 'milquetoast'
    elif not answer1 and not answer2:
        return 'rustic'   

################################################################################################
# GameEvent and Event Classes
################################################################################################
class GameEvent(object):

    event_type = ""

    def __init__(self):
        print("Event created")

# Dialog and Text Parsing. Wraps the print statement with more functionality.
class SpeechEvent(GameEvent):

    speaker = ""
    message = ""
    sleep = 0

    def __init__(self, speaker, message, sleep = 0):
        GameEvent.__init__(self)
        self.speaker = speaker
        self.message = message
        self.sleep = sleep

    ## Not really necessary but helps cut down on object instances
    ## Modify properties instead of creating new object
    ## As a rule of thumb, you probably shouldn't alter the speaker
    ## unless it's a variant of the original speaker
    ## e.g. Player: to Player(enraged): or something
        
    def set_speaker(self, speaker):
        self.speaker = speaker

    def get_speaker(self):
        print(self.speaker)

    # set_message(self)
    def sm(self, message):
        self.message = message;

    # get_message(self)
    def gm(self):
        if self.speaker == "":
            print(self.message)
            time.sleep(self.sleep)
        else:
            print(self.speaker + ": " + self.message)
            time.sleep(self.sleep)

    def set_sleep(self, sleep):
        self.sleep = sleep

# bulk create SpeechEvents
def bulk_speechEvent(speakerList, messageList, sleep = 0):

    listLen = len(speakerList)
    
    for x in range(0, listLen):
        current = SpeechEvent("SpeechEvent", speakerList[x], messageList[x])
        current.pm()
        time.sleep(sleep)

# Wrapped check to see if player responded true or false
def detect_bool(input_string):
    if input_string == "true":
        return True
    elif input_string == "false":
        return False
    else:
        return "repeat"

# Movement parsing

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
# Menus
################################################################################################

class Menu(object):

    def __init__(self):
        print("Menu object")

################################################################################################
# Rooms
################################################################################################

class Room(object):

    name = ""
    description = ""
    exits = ""

    descIndex = 0

    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits
        self.room_name()

    def room_name(self):
        print("You are in the " + self.name)
        print()

    def set_description(self, description):
        self.description = description
        
    def get_description(self):
        print(self.description)
        print()
        
    def show_exits(self): ## Debug
        print(self.exits)

    def add_exits(self, exitsAdded):
        for char in exitsAdded:
            if char not in self.exits:
                self.exits += exitsAdded

    def remove_exits(self, exitsRemoved):
        for char in exitsRemove:
            self.exits.replace(char, "")

################################################################################################
# Items
################################################################################################

class Item(object):

    name = ""
    description = ""
    
    def __init__(self, descriptions):
        print("In progress") 

def game_loop():

    ending = 0

    game_start()

    ## close the game here
    while ending == 0:

        action = input("> There's nothing past this point yet, close the game.")

        if action.lower() == "endgame":
            ending = 1
