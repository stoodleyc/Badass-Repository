#thing that make my code work
from random import randint
Hand = 0
DealerHand = 0
help = ("[I can't be bothered typing an explanation right now so I'll do it later]")

#functions and stuff
def tell_hand():
    global Hand
    print("your hand is... {}!".format(Hand))

def player_turn():
    print("it is now your turn!")
    tell_hand()
    print("would you like to hit or stand?")
    playermove=input()


def round():
    global DealerHand
    global Hand
    Hand = randint(2,20)
    DealerHand = randint(2,20)

    player_turn()

def Game():
    score = 0
    round()

#start screen
print('''▀█████████▄   ▄█          ▄████████  ▄████████    ▄█   ▄█▄      ▄█    ▄████████  ▄████████    ▄█   ▄█▄ 
  ███    ███ ███         ███    ███ ███    ███   ███ ▄███▀     ███   ███    ███ ███    ███   ███ ▄███▀ 
  ███    ███ ███         ███    ███ ███    █▀    ███▐██▀       ███   ███    ███ ███    █▀    ███▐██▀   
 ▄███▄▄▄██▀  ███         ███    ███ ███         ▄█████▀        ███   ███    ███ ███         ▄█████▀    
▀▀███▀▀▀██▄  ███       ▀███████████ ███        ▀▀█████▄        ███ ▀███████████ ███        ▀▀█████▄    
  ███    ██▄ ███         ███    ███ ███    █▄    ███▐██▄       ███   ███    ███ ███    █▄    ███▐██▄   
  ███    ███ ███▌    ▄   ███    ███ ███    ███   ███ ▀███▄     ███   ███    ███ ███    ███   ███ ▀███▄ 
▄█████████▀  █████▄▄██   ███    █▀  ████████▀    ███   ▀█▀ █▄ ▄███   ███    █▀  ████████▀    ███   ▀█▀ 
             ▀                                   ▀         ▀▀▀▀▀▀                            ▀         
hello there, welcome to blackjack.
for help type help anything else will just start the game''')
start=input()
if start == "help":
    print(help)
elif start == "Help":
    print(help)
elif start == "HELP":
    print (help)

#starting the game
Game()
