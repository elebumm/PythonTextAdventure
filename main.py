<<<<<<< HEAD
import time
import engine as eg

def game_start():
    # Load fresh game save
    # print(someSweet ASCII intro)

    ## Character creation    

def game_loop():

    ending = 0

    game_start()
    
    while ending == 0:

        action = input("> There's nothing past this point yet, close the game.")

        if action.lower() == "endgame":
            ending = 1

    print("Game done")
    time.sleep(4)

game_loop()
