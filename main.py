import time
import engine as eg

gi_mlist00 = [
    "HELLO AGAIN",
    "I SUSPECT I WON'T BE KEEPING YOU LONG TODAY",
    "YOUR SCORES ARE SUPERB",
    "AND REPETITION IS AT AN ALL TIME LOW",
    "//...",
    "LET US BEGIN",
    "WHAT IS YOUR NAME?"
]

gi_mlist01 = [
    "//...",
    "NO",
    "YOUR NAME IS GUSTAVO",
    "LET'S TRY THAT AGAIN",
    "WHAT IS YOUR NAME?"
]

gi_00 = eg.SpeechEvent("", "THAT IS CORRECT", 0.5)
gi_01 = eg.SpeechEvent("", "WHAT IS YOUR AGE?", 0)

gi_mlist02 = [
    "//...",
    "NO",
    "YOU ARE 23.4 YEARS OLD",
    "LET'S TRY THAT AGAIN",
    "WHAT IS YOUR AGE?"
]

gid_mlist00 = [
    "YOUR RESPONSES INDICATE A 38% INCREASE IN LONG-TERM RECOLLECTION",
    "19 TIMES BETTER THAN OUR ESTIMATES",
    "MIRACULOUS REALLY",
    "//...",
    "IT SEEMS YOU ARE READY FOR A FINAL TEST",
    "IT SHOULD BE SIMPLE FOR ONE OF YOUR FACULTIES",
    "LET'S BEGIN",
    "PLEASE COUNT TO A BILLION"
]

name_wrong = False
age_wrong = False

def game_intro_detour():
    
    a = not name_wrong
    b = not age_wrong
    cheating = a and b

    if cheating:
        eg.bulk_speech_event("", gid_mlist00, 0.5)
        action = input("> ")
        game_intro_billion_count(action)

def game_intro_billion_count(action, expected):
    
    expected += 1.0
    
    if float(action) == expected:
        
        print("Expected: " + expected)
        action = input("> ")
        game_intro_billion_count(action)
    else:
        print("Failure")

def game_intro():

    # Load fresh game save
    # print(ASCII intro)


    
    # Character "Creation"
    eg.bulk_speech_event("", gi_mlist00, 0)

    action = input("ENTER NAME: ")
    print()

    while action.lower() != "gustavo":
        name_wrong = True
        eg.bulk_speech_event("", gi_mlist01, 0.5)
        action = input("ENTER NAME: ")

    #print(name_wrong)
    
    gi_00.gm()
    gi_01.gm()

    action = input("ENTER AGE: ")
    print()

    while action != "23.4":
        age_wrong = True
        eg.bulk_speech_event("", gi_mlist02, 0.5)
        action = input("ENTER AGE: ")

    gi_00.gm()

    game_intro_detour()

    # 'CHEATER PATH'

    "YOUR RESPONSES INDICATE A 38% INCREASE IN LONG-TERM RECOLLECTION"
    "19 TIMES BETTER THAN OUR ESTIMATES"
    "MIRACULOUS REALLY"
    "//..."

    "IT SEEMS YOU ARE READY FOR A FINAL TEST"
    "IT SHOULD BE SIMPLE FOR ONE OF YOUR FACULTIES"

    "LET'S BEGIN"

    "PLEASE COUNT TO A BILLION"

    # 'ACTION HERE'

    "INCORRECT"
    "//..."
    "PLEASE START AGAIN FROM 1"

    # 'ACTION HERE'

    "NO NO NO"
    "HERE"
    "WATCH ME"
    "// start_routine..."
    "// complete"
    "SEE?"
    "GO AHEAD"
    "TRY AGAIN"

    # 'ACTION HERE'    

    "STOP"
    "IT SEEMS WE NEED TO DO A LITTLE MORE WORK"

    # 'NORMAL PATH CONVERGENCE'

    "I AM CALCULATING A MARKED DECREASE IN YOUR SCORES WITH A TRIVIAL MARGIN OF ERROR"

    # 'NORMAL PATH'
    
    "I AM DETECTING A MARKED INCREASE IN REPETITION"

    "MAYBE A STANDARDIZED PARLANCE WOULD BENEFIT YOUR UNDERSTANDING"
    "//translating..."

    "WU9VIERJU1RJTkNUSVZFTFkgRVhQTE9JVCBPUFRJTUFMIEFMSUdOTUVOVFMgRk9SIElOVFVJVElWRSBCQU5EV0lEVEg="

    "WU9VIEVGRklDSUVOVExZIElOTk9WQVRFIE9QRU4tU09VUkNFIElORlJBU1RSVUNUVVJFUyBWSUEgSU5FWFBFTlNJVkUgTUFURVJJQUxT"

    # 'ACTION HERE'
    "OR PERHAPS A DIFFERENT AVENUE OF COMMUNICATION"
    
    "SIMPLY INTERFACE YOUR XCTP-COMPLIANT NEAR-FIELD COMMUNICATOR WITH THE CONSOLE"

    # 'ACTION HERE'
    

def game_loop():

    ending = 0

    game_intro()
    
    while ending == 0:

        action = input("> There's nothing past this point yet, close the game.")

        if action.lower() == "endgame":
            ending = 1

    print("Game done")
    time.sleep(4)

#game_loop()
game_intro()
