#Yes. I'm aware this is a mess right now. Look it's my first project don't hate. :L

#Imports
import random
import datetime
from re import I
from time import sleep
import sys
# Graphics
load_text1 = """
 /$$      /$$           /$$                                            
| $$  /$ | $$          | $$                                            
| $$ /$$$| $$  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ 
| $$/$$ $$ $$ /$$__  $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$
| $$$$_  $$$$| $$$$$$$$| $$| $$      | $$  \ $$| $$ \ $$ \ $$| $$$$$$$$
| $$$/ \  $$$| $$_____/| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/
| $$/   \  $$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$
|__/     \__/ \_______/|__/ \_______/ \______/ |__/ |__/ |__/ \_______/
                                                                       
"""
load_text2 = """
 ________   ______  
|        \ /      \ 
 \$$$$$$$$|  $$$$$$\\
   | $$   | $$  | $$
   | $$   | $$  | $$
   | $$   | $$  | $$
   | $$   | $$__/ $$
   | $$    \$$    $$
    \$$     \$$$$$$ 
"""

load_text3 = """ 
/$$$$$$$$$$                              /$$                     /$$        /$$$$$$                      /$$                    
|__  $$__/                               |__/                    | $$       /$$__  $$                    |__/                    
   | $$  /$$$$$$   /$$$$$$  /$$$$$$/$$$$  /$$ /$$$$$$$   /$$$$$$ | $$      | $$  \__/  /$$$$$$   /$$$$$$$ /$$ /$$$$$$$   /$$$$$$ 
   | $$ /$$__  $$ /$$__  $$| $$_  $$_  $$| $$| $$__  $$ |____  $$| $$      | $$       |____  $$ /$$_____/| $$| $$__  $$ /$$__  $$
   | $$| $$$$$$$$| $$  \__/| $$ \ $$ \ $$| $$| $$  \ $$  /$$$$$$$| $$      | $$        /$$$$$$$|  $$$$$$ | $$| $$  \ $$| $$  \ $$
   | $$| $$_____/| $$      | $$ | $$ | $$| $$| $$  | $$ /$$__  $$| $$      | $$    $$ /$$__  $$ \____  $$| $$| $$  | $$| $$  | $$
   | $$|  $$$$$$$| $$      | $$ | $$ | $$| $$| $$  | $$|  $$$$$$$| $$      |  $$$$$$/|  $$$$$$$ /$$$$$$$/| $$| $$  | $$|  $$$$$$/
   |__/ \_______/|__/      |__/ |__/ |__/|__/|__/  |__/ \_______/|__/       \______/  \_______/|_______/ |__/|__/  |__/ \______/ 
                                                                                                                                 
"""

game_over_text = """
  /$$$$$$                                           /$$$$$$                               
 /$$__  $$                                         /$$__  $$                              
| $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$       | $$  \ $$ /$$    /$$ /$$$$$$   /$$$$$$ 
| $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$      | $$  | $$|  $$  /$$//$$__  $$ /$$__  $$
| $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$      | $$  | $$ \  $$/$$/| $$$$$$$$| $$  \__/
| $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/      | $$  | $$  \  $$$/ | $$_____/| $$      
|  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$      |  $$$$$$/   \  $/  |  $$$$$$$| $$      
 \______/  \_______/|__/ |__/ |__/ \_______/       \______/     \_/    \_______/|__/ 
"""
game_exit_text = """
  /$$$$$$                            /$$       /$$$$$$$                     
 /$$__  $$                          | $$      | $$__  $$                    
| $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$$      | $$  \ $$ /$$   /$$  /$$$$$$ 
| $$ /$$$$ /$$__  $$ /$$__  $$ /$$__  $$      | $$$$$$$ | $$  | $$ /$$__  $$
| $$|_  $$| $$  \ $$| $$  \ $$| $$  | $$      | $$__  $$| $$  | $$| $$$$$$$$
| $$  \ $$| $$  | $$| $$  | $$| $$  | $$      | $$  \ $$| $$  | $$| $$_____/
|  $$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$$      | $$$$$$$/|  $$$$$$$|  $$$$$$$
 \______/  \______/  \______/  \_______/      |_______/  \____  $$ \_______/
                                                         /$$  | $$          
                                                        |  $$$$$$/          
                                                         \______/ 
"""
you_win_text = """
 /$$     /$$                                      /$$          
|  $$   /$$/                                     |__/          
 \  $$ /$$//$$$$$$  /$$   /$$       /$$  /$$  /$$ /$$ /$$$$$$$ 
  \  $$$$//$$__  $$| $$  | $$      | $$ | $$ | $$| $$| $$__  $$
   \  $$/| $$  \ $$| $$  | $$      | $$ | $$ | $$| $$| $$  \ $$
    | $$ | $$  | $$| $$  | $$      | $$ | $$ | $$| $$| $$  | $$
    | $$ |  $$$$$$/|  $$$$$$/      |  $$$$$/$$$$/| $$| $$  | $$
    |__/  \______/  \______/        \_____/\___/ |__/|__/  |__/
"""

you_lose_text = """

 /$$     /$$                        /$$                                    
|  $$   /$$/                       | $$                                    
 \  $$ /$$//$$$$$$  /$$   /$$      | $$        /$$$$$$   /$$$$$$$  /$$$$$$ 
  \  $$$$//$$__  $$| $$  | $$      | $$       /$$__  $$ /$$_____/ /$$__  $$
   \  $$/| $$  \ $$| $$  | $$      | $$      | $$  \ $$|  $$$$$$ | $$$$$$$$
    | $$ | $$  | $$| $$  | $$      | $$      | $$  | $$ \____  $$| $$_____/
    | $$ |  $$$$$$/|  $$$$$$/      | $$$$$$$$|  $$$$$$/ /$$$$$$$/|  $$$$$$$
    |__/  \______/  \______/       |________/ \______/ |_______/  \_______/
"""
#Create Card Visual
def card_visual(cards, hidden_card = False):

    #Top of card
    visual = ""
    for card in cards:
        visual = visual + "\t _________________"
    #This will print no matter what if card_visual(hidden_card = True). This is so the dealer can later have two cards in his daraw. And you can just cut out the second card as this needs a list object to be passed into it..
    #While still showing two cards. One is the first card drawn the second being what this if statement does. Prints a card not showing any information.  
    if hidden_card:
        visual = visual + "\t _________________"
    print(visual)

    #One line down with card Value
    visual = ""
    for card in cards:
        if card.value == "10":
            visual = visual + "\t$  {}             $".format(card.value)
        else:
            visual = visual + "\t$  {}              $".format(card.value)
    if hidden_card:
        visual = visual + "\t$  {}              $".format("?")
    print(visual)

    #Four lines for card side
    visual = ""
    for line in list(range(0, 4)):
        visual = ""
        for card in cards:
            visual = visual + "\t$                 $"
        if hidden_card:
            visual = visual + "\t$                 $"
        print(visual)

    #Middle of card with Suit Logo
    visual = ""
    for card in cards:
        visual = visual + "\t$        {}        $".format(card.suit)
    if hidden_card:
        visual = visual + "\t$        {}        $".format("?")
    print(visual)

    #Four lines for card side
    visual = ""
    for line in list(range(0, 4)):
        visual = ""
        for card in cards:
            visual = visual + "\t$                 $"
        if hidden_card:
            visual = visual + "\t$                 $"
        print(visual)

    #One line from bottom with card value
    visual = ""
    for card in cards:
        if card.value == "10":
            visual = visual + "\t$             {}  $".format(card.value)
        else:
            visual = visual + "\t$              {}  $".format(card.value)
    if hidden_card:
        visual = visual + "\t$              {}  $".format("?")
    print(visual)

    #Line at bottom
    visual = ""
    for card in cards:
        visual = visual + "\t$_________________$"
    if hidden_card:
        visual = visual + "\t$_________________$"
    print(visual)    
    

#Creates card objects
class Card:
    def __init__(self, suit, value, card_points):
        self.suit = suit
        self.value = value
        self.card_points = card_points

# Card Information
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

suits_unicode = {"Spades": "\u2664", "Hearts": "\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}

cards = ["A", "2", "3", "4", "5", "7", "8", "9", "10", "J", "Q", "K"] 

cards_points = {"A": 11, "2": 2, "3": 2, "4": 2, "5": 2, "6": 2, "7": 2, "8": 2, "9": 2, "10": 2, "J": 10, "Q": 10, "K": 10}

#Creates the card deck using Card class objects.
new_deck = []
def deck_maker(deck):
    for suit in suits:
        for card in cards:
            deck.append(Card(suits_unicode[suit], card, cards_points[card]))
    return deck

#Player Class
class Player:
    def __init__(self, name, player_cards, money = 0, games_played = 0, game_points = 0):
        self.money = money
        self.name = name
        self.games_player = games_played
        self.player_cards = player_cards
        self.game_points = game_points

    def money_add_remove(self, money_amount):
        self.money += money_amount
    
    def add_points(self, points_add):
        self.game_points += points_add

#House Class
class House:
    def __init__(self, name, player_cards, money = 1000000, game_points = 0):
        self.money = money
        self.name = name
        self.player_cards = player_cards
        self.game_points = game_points
    
    def money_add_remove(self, money_amount):
        self.money += money_amount
    
    def add_points(self, points_add):
        self.game_points += points_add


player1 = Player("deafult", [], 1500)
house1 = House("The Terminal Casino", [])

#Play again Fucntion
def play_again():
    play_again1 = input("Would you like to play again? (Yes, No)")
    if play_again1 == "Yes":
        black_jack()
    elif play_again1 == "No":
        sys.exit(game_exit_text)
    else:
        print("Not a valid input")
        play_again()

#Black Jack Game
def black_jack():
    #Reset player and house points and cards
    player1.player_cards = []
    player1.game_points = 0
    house1.game_points = 0
    house1.player_cards = []
    #Creates a deck of cards using deck_maker
    deck_maker(new_deck)

    #Checks if player has busted
    def player_over_21_points():
        if player1.game_points > 21:
            print("You are BUST!")
            print(game_over_text)
            play_again()
        else:
            return
    
    print("Shuffling Cards")
    sleep(1)
    print("Shuffle Noise")
    sleep(1)
    print("Shuff")
    sleep(1)
    print("shuff")
    sleep(1)
    print("Dealing Cards")
    sleep(2)
    #Deal the player 2 cards. And Remove them from the deck.
    while len(player1.player_cards) < 2:
        player_card = random.choice(new_deck)
        player1.player_cards.append(player_card)
        new_deck.remove(player_card)

    
    #Print out the players Cards and points total
    for card in player1.player_cards:
        player1.game_points += card.card_points
    print("Your cards are:")
    card_visual(player1.player_cards)
    print("")
    print("For a total of:")
    print(player1.game_points)
    if player1.game_points == 21:
        print(you_win_text)
        play_again()
    
    #Deal the house two cards. And Remove them from the deck.
    while len(house1.player_cards) < 2:
        player_card = random.choice(new_deck)
        house1.player_cards.append(player_card)
        new_deck.remove(player_card)
    
    #Print out the Houses Cards and current point total while keeping their second card hidden.
    print("")
    print("-------------------------------------------------------------")
    print("The Houses Cards are:")
    card_visual(house1.player_cards[:-1], True)
    for card in house1.player_cards[:-1]:
        house1.game_points += card.card_points
    if house1.game_points == 21:
        card_visual(house1.player_cards)
        print("The house got 21!")
        print(game_over_text)
        play_again()
        

    print("For a Total of:")
    print(house1.game_points)


    #What would the player like to do now?
    def house_at_17():
        print("The dealer stands.")
        print("Checking player and house point total.")
        sleep(2)
        if player1.game_points > house1.game_points:
            print(you_win_text)
            play_again()
        elif house1.game_points > player1.game_points:
            print(you_lose_text)
            print(game_over_text)
            play_again()
        elif house1.game_points == player1.game_points:
            print("Same score.")
            print("You get your bet back.")
            print(game_over_text)
            play_again()
        else:
            return

    def house_hit():
        while house1.game_points < 16:
            print("The house Hits")
            player_card = random.choice(new_deck)
            house1.player_cards.append(player_card)
            new_deck.remove(player_card)
            card_visual(house1.player_cards)
            #Resets house points so the new card can be counted with the old cards.
            house1.game_points = 0
            for card in house1.player_cards:
                house1.game_points += card.card_points
            print("The houses total points is now: ")
            print(house1.game_points)
            if house1.game_points > 21:
                print("House over 21.")
                print(you_win_text)
                play_again()
        house_at_17()


    def house_choice():
        print("Your turn is over. Now for the house.")
        print("The house flips their hidden card")
        card_visual(house1.player_cards)
        house1.game_points = 0
        for card in house1.player_cards:
            house1.game_points += card.card_points
        print("The house now has a total of:")
        print(house1.game_points)
        if house1.game_points <= 16:
            house_hit()
        else:
            house_at_17()


    #Function to hit the player. (Give them a card. Not throw the monitor at them.)
    def hit_me_one_more_time():
        hit_again = input("Would you like to hit again? (Yes / No) ")
        if hit_again == "Yes":
            print("Drawing one more card")
            player_card = random.choice(new_deck)
            player1.player_cards.append(player_card)
            new_deck.remove(player_card)
            print("Your cards are: ")
            card_visual(player1.player_cards)
            print("For a total of: ")
            #Resets players point count so it can recount with the new card!
            player1.game_points = 0
            for card in player1.player_cards:
                player1.game_points += card.card_points
            print(player1.game_points)
            #Check if the new card busted the player. If not asks if player wants to hit agian.
            if player1.game_points > 21:
                player_over_21_points()
            else:
                hit_me_one_more_time()
        elif hit_again ==  "No":
            house_choice()
        else:
            print("Not a valid input.")
            hit_me_one_more_time()
    
    def action_hit():
        print("Drawing One more Card.")
        player_card = random.choice(new_deck)
        player1.player_cards.append(player_card)
        new_deck.remove(player_card)
        print("Your cards are: ")
        card_visual(player1.player_cards)
        print("For a total of: ")
        player1.game_points = 0
        for card in player1.player_cards:
            player1.game_points += card.card_points
        print(player1.game_points)
        sleep(1)
        if player1.game_points > 21:
            player_over_21_points()
        else:
            hit_me_one_more_time()    
        hit_me_one_more_time()

    def action_stand():
        print("You stand!")
        house_choice()





    def round_1_choice():
        player_choice = input("What would you like to do? (Stand, Surrender, Hit, Double Down): ")
        if player_choice == "Surrender":
            print(game_over_text)
            print("Half of inital Bet Back to Player")
            play_again = input("Would you like to play again? (Yes, No): ")
            if play_again == "Yes":
                black_jack()
        elif player_choice == "Hit":
            action_hit()
        elif player_choice == "Double Down":
            print("Betting not implemented.")
            action_hit()
        elif player_choice == "Stand":
            action_stand()
        else:
            print("That's not a valid option.")
            round_1_choice()
            
    round_1_choice()
#Ready to play 
print(load_text1)
print(load_text2)
print(load_text3)
play_game = input("Are you wanting to play? - (Yes or No): ")
if play_game == "Yes":
    what_game_start = input("What game would you like to play? (Blackjack or Blackjack): ")
if what_game_start == "Blackjack":
    black_jack()







 

