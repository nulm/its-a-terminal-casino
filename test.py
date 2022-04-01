suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

suits_unicode = {"Spades": "\u2664", "Hearts": "\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}

cards = ["A", "2", "3", "4", "5", "7", "8", "9", "10", "J", "Q", "K"] 

cards_points = {"A": 11, "2": 2, "3": 2, "4": 2, "5": 2, "6": 2, "7": 2, "8": 2, "9": 2, "10": 2, "J": 10, "Q": 10, "K": 10}

print("\t _________________")
print("\t$  {}              $".format(cards[0]))
print("\t$                 $")
print("\t$                 $")
print("\t$                 $")
print("\t$                 $")
print("\t$        {}        $".format(suits_unicode["Diamonds"]))
print("\t$                 $")
print("\t$                 $")
print("\t$                 $")
print("\t$                 $")
print("\t$              {}  $".format(cards[0]))
print("\t$_________________$")