#Imports
import random
import datetime
from time import sleep
# Graphic to load when starting game.
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

#Create Card Visual
def card_visual(cards, hidden_card = False):

    #Top of card
    visual = ""
    for card in cards:
        visual = visual + "\t _________________"
    #This will print no matter what if card_visual(hidden_card = True). This is so the dealer can later have two cards in his daraw. And you can just cut it out while still passsing in a list object of just one card. 
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

#Black Jack Game
def black_jack():
    #Creates a deck of cards using deck_maker
    deck_maker(new_deck)


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
    print("For a Total of:")
    for card in house1.player_cards[:-1]:
        house1.game_points += card.card_points
    print(house1.game_points)

#Ready to play 
print(load_text1)
print(load_text2)
print(load_text3)
play_game = input("Are you wanting to play? - (Yes or No): ")
if play_game == "Yes":
    what_game_start = input("What game would you like to play? (Blackjack or Blackjack): ")
if what_game_start == "Blackjack":
    black_jack()







 

