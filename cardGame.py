'''
Importing various helper modules.
'''

from Player import Player
from UserManagement import UserManagement
from CardDeck import CardDeck
import sys
import json
import time
import os

# Deck attribute defined to Store and track list of cards while playing the game.
deck = []

# Player Objects define. We need two players
player1 = Player()
player2 = Player()
# Created and instance of UserManagement
userMgmt = UserManagement()
# Created and instance of CardDeck, which returns deck of cards
cd = CardDeck()

# Main function to start the game. Checks to see if two players are avalable in the game. If not, the game will not proceed.
def startGame():
    # Checks to see if player1 is defined
    if not player1.name:
        print("\n            ######      WELCOME    ######            \n")
        print(" 1. To play the game, ensure you're logged in\n")
        print(" 2. Choose register Option, if not already registered\n ")
        print(" 3. Type login or register to begin\n")
        print(" 4. Want to quit the game, type quit\n")

        if not player1.name and not player2.name:
            choice = input("Enter Your Choice: ")
            if len(choice) > 0:
                if choice.lower()[0] == "r":
                    userMgmt.registerUser()
                    startGame()
                elif choice.lower()[0] == "l":
                    if not player1.name:
                        player1.name = userMgmt.loginUser()
                        startGame()
                    else:
                        player2.name = userMgmt.loginUser()
                elif choice.lower()[0] == "q":
                    sys.exit()
                else:
                    startGame()
            else:
                startGame()
    else:
        # Checks to see if player2 is defined
        if not player2.name:
            print("\nLogin for Second Player")
            player2.name = userMgmt.loginUser()


# Helper function to sort top 5 winners, based on index 1 of tuple.
def sort_item(item):
    return item[1]

 # the name of the module that starts the program is always __main__ 

if __name__ == '__main__':
    startGame()

# If both players are defined, we start the game
if player1.name and player2.name:
    os.system("clear")
    print("Let's Begin game for players " +
          player1.name + " VS " + player2.name + "\n")
    time.sleep(2)
    # Gets a list of deck
    deck = cd.generateDeck()
    # we run the loop only for half of length of deck, since 2 cards are popped each time
    for x in range(int(len(deck)/2)):
        player1.card = deck.pop(0)
        player2.card = deck.pop(0)

        if player1.card[0] == player2.card[0]:  # Colors are same
            if player1.card[1] > player2.card[1]:
                player1.score = player1.score + 1
                player1.deck.append(player1.card)
                player1.deck.append(player2.card)
            else:
                player2.score = player2.score + 1
                player2.deck.append(player2.card)
                player2.deck.append(player1.card)
        elif player1.card[0] == "Red" and player2.card[0] == "Black":
            player1.score = player1.score + 1
            player1.deck.append(player1.card)
            player1.deck.append(player2.card)
        elif player1.card[0] == "Yellow" and player2.card[0] == "Red":
            player1.score = player1.score + 1
            player1.deck.append(player1.card)
            player1.deck.append(player2.card)
        elif player1.card[0] == "Black" and player2.card[0] == "Yellow":
            player1.score = player1.score + 1
            player1.deck.append(player1.card)
            player1.deck.append(player2.card)

    print("#############   SCORES  #############\n")
    print(f"Player1 :{player1.score}  vs. Player2 :${player2.score}")
    print("\n###################################\n")
    print(" <<<<<<<<--------- Winner of this game is  --------->>>>>>>> \n")
    time.sleep(2)

    # check the length of deck for each player and store the winner by calling the storeWinner helper function
    if len(player1.deck) > len(player2.deck):
        userMgmt.storeWinner(player1.name, player1.deck, len(player1.deck))
        print(f"---- {player1.name} ---- \n")
    else:
        userMgmt.storeWinner(player2.name, player2.deck, len(player2.deck))
        print(f"---- {player2.name} ---- \n")

    print(" <<<<<<<<--------- Our Top 5 Winners are  --------->>>>>>>> \n")
    winners = userMgmt.readWinner()
    # Sorts the top 5 winner by calling the default sort function and passing our custom sort method defined above.
    winners.sort(key=sort_item, reverse=True)
    for winner in winners[:5]:
        print(winner)

    print("\n\n")
