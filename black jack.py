#thing that makes my code work
from random import randint
unknown = ('''
sorry I don't recognize that answer please try again
''')

#functions
#minor functions that are only functions for my covenience
def tell_hand():
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
        Continue()
        win()
    else:
        Continue()
        if Stand == 1:
            stand()
        else:
            player_turn()

def DealerStand():
    print("The dealer is standing!")
    Continue()
    if Stand == 1:
        if Hand > DealerHand:
            win()
        elif Hand < DealerHand:
            lose()
        elif Hand == DealerHand:
            draw()
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
    print('''round {} start!
    '''.format(Round))
    Stand = 0
    Hand = randint(2,20)
    DealerHand = randint(2,20)
    player_turn()

def Game():
    global score
    global Round
    Round = 1
    score = 0
    round()

def lose():
    global hisc
    global score
    print("")
    print("your hand was {}".format(Hand))
    print("the dealers hand was {}".format(DealerHand))
    #highscore things
    hisc = open('highscore.txt',"r")

    hisc = open('highscore.txt', "w")
    hisc.write(str(score))
    hisc.close()

def win():
    global score
    global Round
    score = score + 1
    Round = Round + 1
    print("")
    print("your hand was {}".format(Hand))
    print("the dealers hand was {}".format(DealerHand))
    print ('''██    ██  ██████  ██    ██     ██     ██ ██ ███    ██ ██ 
 ██  ██  ██    ██ ██    ██     ██     ██ ██ ████   ██ ██ 
  ████   ██    ██ ██    ██     ██  █  ██ ██ ██ ██  ██ ██ 
   ██    ██    ██ ██    ██     ██ ███ ██ ██ ██  ██ ██    
   ██     ██████   ██████       ███ ███  ██ ██   ████ ██ 
                                                         ''')
    print("[your current score is... {} wins!]".format(score))
    input('''Press Enter to start round {}...
    '''.format(Round))
    round()

def draw():
    global Round
    global score
    Round = Round + 1
    print("")
    print('''██████  ██████   █████  ██     ██ 
██   ██ ██   ██ ██   ██ ██     ██ 
██   ██ ██████  ███████ ██  █  ██ 
██   ██ ██   ██ ██   ██ ██ ███ ██ 
██████  ██   ██ ██   ██  ███ ███  ''')
    print("you tied at {}".format(Hand))
    print("[your current score is... {} wins.]".format(score))
    input('''press Enter to start round {}...
    '''.format(Round))
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
for help type help otherwise press enter start the game''')
start=input()
if start.lower() == "help":
    help()

#starting the game
Game()
