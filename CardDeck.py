import random

deck = []
card_colors = ["Red", "Yellow", "Black"]
card_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# Generates a Deck of card based on numbers and card_colors
# Returns a deck of cards to the calling function
class CardDeck:
    def __init__(self):
        pass

    def generateDeck(self):
        for color in card_colors:
            for card_no in card_numbers:
                deck.append([color, card_no])
        random.shuffle(deck)
        return deck
