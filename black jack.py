#thing that makes my code work
from random import randint
unknown = ('''
sorry I don't recognize that answer please try again
''')

#functions
#minor functions that are only functions for my covenience
def tell_hand():
    global Hand
    print("your hand is... {}!".format(Hand))

def Continue():
    input('''
    Press Enter to continue...''')

def help():
    print("[I can't be bothered typing an explanation right now so I'll do it later]")
    print('''
    Press Enter to start...''')
    input()

#the moves
def hit():
    global Hand
    Hand = Hand + randint(1,10)
    tell_hand()
    if Hand > 21:
        lose()
    else:
        Continue()
        dealer_turn()

def stand():
    global Stand
    Stand = 1
    print("you are standing on {}.".format(Hand))
    dealer_turn()

def DealerHit():
    global DealerHand
    DealerHand = DealerHand + randint(1,10)
    print("Dealer hits!")
    if DealerHand> 21:
        win()
    else:
        Continue()
        player_turn()

def DealerStand():
    global Stand
    global Hand
    global DealerHand
    print("The dealer is standing!")
    Continue()
    if Stand == 1:
        if Hand > DealerHand:
            win()
        elif Hand < DealerHand:
            lose()
        elif Hand == DealerHand:
            print("stuff")
    else:
        player_turn()


#the turns
def player_turn():
    global unknown
    global Stand
    print("")
    if stand == 1:
        stand()
    else:
        print("it is now your turn!")
        tell_hand()
        print("would you like to hit or stand?")
        playermove=input()
        if playermove.lower() == "hit":
            hit()
        elif playermove.lower() == "stand":
            stand()
        else:
            print (unknown)
            player_turn()

def dealer_turn():
    global DealerHand
    print("")
    print ("dealer's turn!")
    if DealerHand < 17:
        DealerHit()
    else:
        DealerStand()

#the game states
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

def Game():
    global score
    score = 0
    round()

def lose():
    print ("shame you lose!")

def win():
    global score
    score = score + 1
    print("good job you've won a whole {} times without losing".format(score))
    input('''Press Enter to start round {}...
    '''.format(score + 1))
    round()

def draw():
    global score

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
if start.lower() == "help":
    help()

#starting the game
Game()
