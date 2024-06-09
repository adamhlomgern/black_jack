# BLACK JACK #


# Modules:
import random
from art import logo



# Lists:
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

def start_game():
    print(logo)
    print("Welcome to the bestest of all Blackjack games!")

    user_hand = []
    computer_hand = []

    for _ in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())

    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)

    print(f"Your cards: {user_hand}, current score: {user_score}")
    print(f"Computers first card: {computer_hand[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        print(compare_scores(user_score, computer_score))
    else:
        while input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            user_hand.append(deal_card())
            user_score = calculate_score(user_hand)
            print(f"Your cards: {user_hand}, current score: {user_score}")
            if user_score > 21:
                break
        while computer_score != 0 and computer_score < 17:
            computer_hand.append(deal_card)
            computer_score = calculate_score(computer_hand)

        print(f"Your final hand: {user_hand}, final score: {user_score}")
        print(f"Computers final hand: {computer_hand}, final score: {computer_score}")
        print(compare_scores(user_score, computer_score))



# Rules: 
"""
1. Objective: The goal is to have a hand value as close to 21 as possible without exceeding it.
2. Card Values:
    - Cards 2-10 are worth their face value.
    - Face cards (Jack, Queen, King) are each worth 10 points.
    - Aces can be worth either 1 or 11 points, depending on which value helps the hand the most without exceeding 21.
3. Initial deal:
    - Both the player and the dealer are dealt two cards. The players cards are both face up, while the dealer has one card face up and one face down.
4. Blackjack:
    - A hand with an Ace and a 10-value card (10, Jack, Queen, or King) is called a "Blackjack" and is an automatic win unless both the player and dealer have Blackjack, resulting in a tie.
5. Player's turn:
    - The player can choose to "hit" (take another card) or "stand" (keep their current hand).
    - The player can hit as many times as they want until they choose to stand or their hand value exceeds 21 (busts), which results in an automatic loss.
6. Dealer's turn:
    - The dealer reveals their hidden card.
    - The dealer must hit until their hand value is 17 or higher.
7. Winning:
    - If the player's hand value exceeds 21, the player busts and loses.
    - If the dealer's hand value exceeds 21, the dealer busts and the player wins.
    - If neither busts, the hand with the value closest to 21 wins.
    - In the events of a tie (same hand value), the game is a push and the player's bet is returned.
"""


# Main execution
if __name__ == "__main__":
    start_game()