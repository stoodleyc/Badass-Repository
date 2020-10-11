#thing that makes my code work
from random import randint

#variables for convenience
unknown = ('''
sorry I don't recognize that answer please try again
''')
Hit = list(["hit","h","ht","hir","hi","hiit","hat","hitt","htt","it","more","card","gime",])
STAND = list(["stand","s","stnd","stad","staand","sand","tand","stan","sta","std","st"])
Help = list(["help","hilp","hlp","hellp","helpp","help me","teach me","I understand nothing","tutorial","how to play","htp"])
Exit = list(["exit","e","end","exitt","exxit","exiit","stop","ext","exi","eit","leave","kill"])

#functions
#minor functions that are only functions for my covenience
def tell_hand():
    print("your hand is... {}!".format(Hand))

def Continue():
    input('''
    Press Enter to continue...''')

def help():
    print('''- the aim of the game is to get as high a number as possible without  passing 21
- hit means you add to your number
- stand means you do nothing for the rest of the round
- you are competing against the dealer''')
    print('''
    Press Enter to start...''')
    input()
#functions for actions
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

#functions for turns
def player_turn():
    global unknown
    global Stand
    global Hit
    global STAND
    print("")
    if Stand == 1:
        stand()
    else:
        print("it is now your turn!")
        tell_hand()
        print("would you like to hit or stand?")
        playermove=input()
        if playermove.lower() in Hit:
            hit()
        elif playermove.lower() in STAND:
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

#functions for game states
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
    global save
    global score
    global Exit
    print("")
    print('''▓██   ██▓ ▒█████   █    ██     ██▓     ▒█████    ██████ ▓█████ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓██▒    ▒██▒  ██▒▒██    ▒ ▓█   ▀ 
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██░    ▒██░  ██▒░ ▓██▄   ▒███   
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ▒██░    ▒██   ██░  ▒   ██▒▒▓█  ▄ 
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░██████▒░ ████▓▒░▒██████▒▒░▒████▒
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░    ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░ ░   ░ ░ ░ ▒  ░  ░  ░     ░   
 ░ ░         ░ ░     ░            ░  ░    ░ ░        ░     ░  ░
 ░ ░                                                           ''')
    print("your hand was {}".format(Hand))
    print("the dealers hand was {}".format(DealerHand))
    #sets the highscore
    save = open('highscore.txt',"r")
    hisc = int(save.read())
    save.close
    if score > hisc:
        print("[NEW HIGHSCORE!]")
        print("your score is... {}!".format(score))
        save = open('highscore.txt', "w")
        save.write(str(score))
        save.close()
    else:
        print("[your score is {}]".format(score))
        print("[your highscore is {}]".format(hisc))
    #continue
    print("")
    playagain=input('''press enter to play again or type exit to stop
    ''')
    if playagain.lower() in Exit:
        exit()
    else:
        print("")
        Game()

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
if start.lower() in Help:
    help()

#starting the game
Game()
