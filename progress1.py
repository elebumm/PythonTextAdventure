import time

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
# CLASS: Room
#
# DESCRIPTION: The Room base class.
#
################################################################################################

class Player(object):

    ## Personally I wouldn't like health or stats in a text-based game
    ## I don't mind simple attributes though
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

    def get_name(self): ## debugging, might be useful for
        print(self.name)

    def set_ability(self, abilities_key):
        self.ability = self.abilities[abilities_key]
        print(self.ability)

    def get_ability(self):
        return self.ability

class GameEvent(object):

    event_type = ""

    def __init__(self, event_type):
        self.event_type = event_type
        #print(self.event_type)

class SpeechEvent(GameEvent):

    speaker = ""
    message = ""
    sleep = 0

    def __init__(self, event_type, speaker, message, sleep = 0):
        GameEvent.__init__(self, event_type)
        self.speaker = speaker
        self.message = message
        self.sleep = sleep

    def pm(self): # short for print_message
        if self.speaker == "":
            print(self.message)
            time.sleep(self.sleep)
        else:
            print(self.speaker + ": " + self.message)
            time.sleep(self.sleep)

    def set_sleep(self, sleep):
        self.sleep = sleep

## bulk create speech events
def bulk_speechEvent(speakerList, messageList, sleep):

    listLen = len(speakerList)
    
    for x in range(0, listLen):
        current = SpeechEvent("SpeechEvent", speakerList[x], messageList[x])
        current.pm()
        time.sleep(sleep)
        

class Room(object):

    name = ""
    descriptions = []
    exits = "ns"

    descIndex = 0

    def __init__(self, name, descriptions, exits):
        self.name = name
        self.descriptions = descriptions
        self.exits = exits
        self.room_name()

    def room_name(self):
        print("You are in the " + self.name)
        print()

    ## Examine a room and change it's description from
    def examine(self):
        print(self.descriptions[self.descIndex])
        print()

    ## Perhaps decide between having a description list or...
    def change_descIndex(self, descIndex):
        self.descIndex = descIndex

    ## Just have a set_description method with a description that you can set on the fly.
    ## Current solution is to add a description to the descriptions list
    ## and set the descIndex to the last element.
    def set_description(self, description):
        self.descriptions.append(description)
        self.descIndex = len(self.descriptions) - 1

    ## Alter the movement options for the parser.
    ## show_exits is a debugging method
    def show_exits(self):
        print(self.exits)

    def add_exits(self, exitsAdded):
        for char in exitsAdded:
            if char not in self.exits:
                self.exits += exitsAdded

    def remove_exits(self, exitsRemoved):
        for char in exitsRemove:
            self.exits.replace(char, "")

class Item(object):

    name = ""
    descriptions = []

    def __init__(self, descriptions):
        print("In progress")

game_start_0 = SpeechEvent("SpeechEvent", "", "WHAT IS YOUR NAME?", 2)
game_start_1 = SpeechEvent("SpeechEvent", "", "NO.", 2)
game_start_2 = SpeechEvent("SpeechEvent", "", "YOUR NAME IS JEAN.", 2)
game_start_3 = SpeechEvent("SpeechEvent", "", "GOOD.", 2)
game_start_4 = SpeechEvent("SpeechEvent", "", "NOW.", 2)
game_start_5 = SpeechEvent("SpeechEvent", "", "ANSWER true OR false TO THE FOLLOWING:", 3)
game_start_6 = SpeechEvent("SpeechEvent", "", "YOU DISTINCTIVELY EXPLOIT OPTIMAL ALIGNMENTS FOR INTUITIVE BANDWIDTH.", 3)
game_start_7 = SpeechEvent("SpeechEvent", "", "---", 5)
game_start_8 = SpeechEvent("SpeechEvent", "", "YOU EFFICIENTLY INNOVATE OPEN-SOURCE INFRASTRUCTURES VIA INEXPENSIVE MATERIALS.", 3)
game_start_9 = SpeechEvent("SpeechEvent", "", "---", 5)
game_start_10 = SpeechEvent("SpeechEvent", "", "THANK YOU.", 2)
game_start_11 = SpeechEvent("SpeechEvent", "", "THAT CONCLUDES THE INTERVIEW PHASE.", 3)
game_start_12 = SpeechEvent("SpeechEvent", "", "YOU'RE HIRED, MR. JEAN.", 4)
game_start_13a = SpeechEvent("SpeechEvent", "", "ALTHOUGH, FOR SOMEONE LIKE YOU, IT WON'T BE EASY.", 5)
game_start_13b = SpeechEvent("SpeechEvent", "", "YOU'LL FIT RIGHT IN.", 5)
game_start_13c = SpeechEvent("SpeechEvent", "", "DON'T TURN YOUR BACK ON THE BODY.", 5)
game_start_13d = SpeechEvent("SpeechEvent", "", "I EXPECT YOU'LL DO MANY GREAT THINGS HERE.", 5)

def detect_bool(input_string):
    if input_string == "true":
        return True
    elif input_string == "false":
        return False
    else:
        return "repeat"

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
        


def game_start():
    # Load fresh game save
    # print(someSweet ASCII intro)

    ## "Choose" your name
    game_start_0.pm()
    action = input("ENTER NAME: ")
    nameIsJean = action

    while nameIsJean != "jean":
        game_start_1.pm()
        game_start_2.pm()
        game_start_0.pm()
        action = input("ENTER NAME: ")
        nameIsJean = action

    game_start_3.pm()

    ## Answer 2 questions to decide ability
    ## There are 4 total outcomes for ability (considering true/false answers)
    ## If you add more questions, then I need to make a bigger
    ## abilities dictionary in the Player class
    game_start_4.pm()
    game_start_5.pm()
    game_start_6.pm()
    action = input("> ")
    firstDecision = detect_bool(action)

    while firstDecision == "repeat":
        game_start_6.set_sleep(1)
        game_start_6.pm()
        action = input("> ")
        firstDecision = detect_bool(action)

    game_start_7.pm()
    game_start_8.pm()
    action = input("> ")
    secondDecision = detect_bool(action)

    while secondDecision == "repeat":
        game_start_8.set_sleep(1)
        game_start_8.pm()
        action = input("> ")
        secondDecision = detect_bool(action)

    game_start_9.pm()
    game_start_10.pm()
    game_start_11.pm()
    game_start_12.pm()

    ##change last message based on answers
    player = Player()
    player.set_ability(calculate_ability(firstDecision, secondDecision))

    if player.get_ability() == 0:
        game_start_13a.pm()
    elif player.get_ability() == 1:
        game_start_13b.pm()
    elif player.get_ability() == 2:
        game_start_13c.pm()
    elif player.get_ability() == 3:
        game_start_13d.pm()
    

def game_loop():

    ending = 0

    game_start()

    ## close the game here
    while ending == 0:

        action = input("> There's nothing past this point yet, close the game.")

        if action.lower() == "endgame":
            ending = 1

game_loop()
    

medBayDesc = ["You awake in a comfy bed to the ministrations of an auto-nurse and a bright glare.\n"
            "White linens. White walls. White lights.\n"
            "There is a white door at the north end of the room.\n"
            "You are in the medical bay of the /OBLIVIOUS/.\n"
            "You wave away the medical robot and climb out of bed.",
              "Second message",
              "Hello"]

medicalBay = Room("Medical Bay", medBayDesc, "nsew")
medicalBay.examine()

medicalBay.set_description("This description did not exist til now")
medicalBay.examine()

# Bulk speech event is cool :)
#
#speakers1 = ["Romet", "Not Romet"]
#messages1= ["Greetings", "Hello, interloper"]
#
#bulk_speechEvent(speakers1, messages1, 1)
#
