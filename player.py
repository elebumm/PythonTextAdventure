################################################################################################
#
# Use this as a reference for importing. Instead of "from player import *" use:
#
# from player import Player
#
# IN THIS MODULE:
#
# CLASSES:
#   * Player
#
# METHODS:
#   * calculate_ability
#
################################################################################################

from creature import Creature

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

player_one = Player("poops mcgee", "poopmancer", "humanoid")
player_one.get_name()
player_one.get_ability() ## Fix this line. Setting ability should be in __init__
