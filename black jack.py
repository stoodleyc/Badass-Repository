#I apoligise in advance for anyone trying to read my code

#thing that makes my code work
from random import randint
Hand = 0
DealerHand = 0
unknown = ('''
sorry I don't recognize that answer please try again
''')

#functions and stuff
def tell_hand():
    global Hand
    print("your hand is... {}!".format(Hand))

def player_turn():
    global unknown
    print("it is now your turn!")
    tell_hand()
    print("would you like to hit or stand?")
    playermove=input()
    if playermove == "hit":
        hit()
    elif playermove == "Hit":
        hit()
    elif playermove == "HIT":
        hit()
    elif playermove == "stand":
        stand()
    elif playermove == "Stand":
        stand()
    elif playermove == "STAND":
        stand()
    else:
        print (unknown)
        player_turn()

def dealer_turn():


def round():
    global DealerHand
    global Hand
    global Stand
    print('''game start!
    ''')
    Stand = 0
    Hand = randint(2,20)
    DealerHand = randint(2,20)
    player_turn()

def hit():
    global Hand
    Hand = Hand + randint(1,10)
    tell_hand()
    if Hand > 21:
        lose()
    else:

def stand():
    global Stand
    Stand = 1
    print("you are standing")

def Game():
    global score
    score = 0
    round()

def help():
    print("[I can't be bothered typing an explanation right now so I'll do it later]")
    print('''
    type anything to start!''')
    input()

def lose():
    print ("shame you lose!")

def win():
    global score
    score = score + 1
    print("good job you've won a whole {} times in a row".format(score))

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
    help()
elif start == "Help":
    help()
elif start == "HELP":
    help()

#starting the game
Game()
