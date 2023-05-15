#Author: Mevin Moncy

import random
from replit import clear
from art import logo

def deal_card():
    """Selects a random card from the deck and returns it."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


def calculate_score(cards):
    """Calculates the score based on the given list of cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """Compares the scores of the user and computer and determines the outcome of the game."""
    if user_score == computer_score:
        return "\n Draw! \n "
    elif computer_score == 0:
        return "\n You Lose! \n"
    elif user_score == 0:
        return "\n You Win! \n"
    elif user_score > 21:
        return "\n You went over, you lose! \n"
    elif computer_score > 21:
        return "\n Computer went over, you win! \n"
    elif user_score > computer_score:
        return "\n You Win! \n"
    else:
        return "\n You Lose! \n"


def play_again():
    """Starts a new game of Blackjack."""
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal two cards to each player
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        # Calculate scores
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        # Check if the game is over
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
            print("Game Over!")
        else:
            user_should_deal = input("Type 'y' to get another card or 'n' to pass: ")
            if user_should_deal.lower() == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Let the computer draw cards until the score is at least 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Display final hands and scores
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play Blackjack? Type 'y' for yes or 'n' for no: ").lower() == "y":
    clear()
    play_again()
