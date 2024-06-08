# BLACK JACK


# Modules:
import random
from art import logo



# Variables:
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
computer_hand = []



# Functions
def deal_card():
    """Returns a random card from the deck."""
    return random.choice(deck)

def calculate_score(hand):
    """Calculates the score of a given hand."""
    if sum(hand) == 21 and len(hand) == 2:
        return 0 #Represents a Blackjack
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare_scores(user_score, computer_score):
    """Compares user and computer scores and returns the result."""
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"



# Rules: