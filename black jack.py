#thing that makes my code work
from random import randint
unknown = ('''
sorry I don't recognize that answer please try again
''')

#functions
#minor functions that aren't very important
def tell_hand():
    global Hand
    print("your hand is... {}!".format(Hand))

def help():
    print("[I can't be bothered typing an explanation right now so I'll do it later]")
    print('''
    type anything to start!''')
    input()

#the moves
def hit():
    global Hand
    Hand = Hand + randint(1,10)
    tell_hand()
    if Hand > 21:
        lose()
    else:
        input('''type anything to continue.
        ''')
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
        input('''type anything to continue.
        ''')
        player_turn()

def DealerStand():
    print("nice")

#the turns
def player_turn():
    global unknown
    global Stand
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
    global dealer_stand
    global DealerHand
    if dealer_stand == 1:
        print ("the deala be standin")
    print('''
    ''')
    print ("dealer's turn!")
    if DealerHand < 17:
        DealerHit()
    else:
        print("dealerstand")

#the game states
def round():
    global DealerHand
    global Hand
    global Stand
    global dealer_stand
    print('''game start!
    ''')
    Stand = 0
    dealer_stand = 0
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
if start.lower() == "help":
    help()

#starting the game
Game()
