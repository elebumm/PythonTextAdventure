import time

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

    

class ItemContainer(Node):

    def __init__(self, name, description):
        Node.__init__(self)
                
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
                    
    if isinstance(destination, (Node, Creature)): ## Later add Container, Room, etc.
        parentnode = target.parent
        parentnode.children.remove(target)
        destination.addChild(target)
    else:
        print("Sorry. The destination cannot contain anything.")
        
class Room(Node):

    def __init__(self, name, description, exits):
        Node.__init__(self, name, description)
        self.exits = exits
        self.get_name()

    def get_name(self):
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

class Item(Leaf):
    
    def __init__(self, name, description):
        Leaf.__init__(self, name, description)

class Creature(object):

    def __init__(self, name, description, creature_type):
        self.name = name
        self.description = description
        self.creature_type = creature_type
        self.isAlive = True 


class Player(Creature):

    abilities = {'rustic': 0, 'soder': 1, 'bebop': 2, 'choral': 3}
    ability = 0

    visibility = "visible" #Yes, for stealth and such. Maybe change to an integer value of 0 - 100

    def __init__(self, name, description, creature_type):
        Creature.__init__(self, name, description, creature_type)
        print("Debug: Player created")
        print()

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


# CLEAN THIS UP START#

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
# You can pass in empty lists for speaker_list and a single sleep value to sleep_list
# and their lists will be created from the length of message_list
def bulk_speech_event(speaker_list, message_list, wait_list):

    new_speaker = []
    new_wait = []

    if type(speaker_list) is str:
        for m in message_list:
            new_speaker.append(speaker_list)
    else:
        new_speaker = speaker_list

    if type(wait_list) is int or type(wait_list) is float:
        for m in message_list:
            new_wait.append(wait_list)
    else:
        new_wait = wait_list
    
    mlist_len = len(message_list)
    
    for x in range(0, mlist_len):
        current = SpeechEvent(new_speaker[x], message_list[x])
        current.gm()
        time.sleep(new_wait[x])

    print()

# Wrapped check to see if player responded true or false
def action_is_bool(input_string, desired_bool):

    for db in desired_bool:
        if input_string.lower() == db.lower():
            return True
            break
        else:
            return False
            
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

# CLEAN THIS UP END #
