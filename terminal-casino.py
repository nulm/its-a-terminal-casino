#Improts
import random
import datetime

from more_itertools import value_chain

#Deck Maker

#Create Card Visual
def visual_card(cards, hidden_card):

    #Top of card
    visual = ""
    for card in cards:
        visual = visual + "\t _________________"
    if hidden_card:
        visual = "\t _________________"
    print(visual)

    #One line down with card Value
    visual = ""
    for card in cards:
        visual = visual + "\t$  {}              $".format(cards[0])
    if hidden_card:
        visual = visual + "\t$  {}              $".format("?")
    print(visual)

    #Four lines for card side
    visual = ""
    for card in cards:
        visual = visual + "\t$                 $"
    if hidden_card:
        visual = visual + "\t$                 $"
    print(visual)

    visual = ""
    for card in cards:
        visual = visual + "\t$                 $"
    if hidden_card:
        visual = visual + "\t$                 $"
    print(visual)
    
    visual = ""
    for card in cards:
        visual = visual + "\t$                 $"
    if hidden_card:
        visual = visual + "\t$                 $"
    print(visual)
    
    visual = ""
    for card in cards:
        visual = visual + "\t$                 $"
    if hidden_card:
        visual = visual + "\t$                 $"
    print(visual)

    #Middle of card with Suit Logo
    visual = ""
    for card in cards:
        visual = visual + "\t$        {}        $".format(suits_unicode["Diamonds"])
    if hidden_card:
        visual = visual + "\t$        {}        $".format("?")
    print(visual)

 #Four lines for card side
    visual = ""
    for card in cards:
        visual = visual + "\t$                 $"
    if hidden_card:
        visual = visual + "\t$                 $"
    print(visual)

    visual = ""
    for card in cards:
        visual = visual + "\t$                 $"
    if hidden_card:
        visual = visual + "\t$                 $"
    print(visual)
    
    visual = ""
    for card in cards:
        visual = visual + "\t$                 $"
    if hidden_card:
        visual = visual + "\t$                 $"
    print(visual)
    
    visual = ""
    for card in cards:
        visual = visual + "\t$                 $"
    if hidden_card:
        visual = visual + "\t$                 $"
    print(visual)

    #One line from bottom with card value
    for card in cards:
        visual = visual + "\t$              {}  $".format(cards[0])
    if hidden_card:
        visual = visual + "\t$              {}  $".format("?")
    print(visual)    
    
    #Bottom of card
    visual = ""
    for card in cards:
        visual = visual + "\t$_________________$"
    if hidden_card:
        visual = visual + "\t$_________________$"




suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

suits_unicode = {"Spades": "\u2664", "Hearts": "\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}

cards = ["A", "2", "3", "4", "5", "7", "8", "9", "10", "J", "Q", "K"] 

cards_points = {"A": 11, "2": 2, "3": 2, "4": 2, "5": 2, "6": 2, "7": 2, "8": 2, "9": 2, "10": 2, "J": 10, "Q": 10, "K": 10}

#Creates card objects
class Card:
    __init__(self, suit, value, card_points):
    self.suit = suit
    self.value = value
    self.card_points = card_points

