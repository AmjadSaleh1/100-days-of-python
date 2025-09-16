import random
from art import logo

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_card = []
dealer_card = []
Game_ends = False


def deal_card():
    random_card = random.choice(cards)
    return random_card


def update_score(cards):
    """this function takes a list of cards and calculate the score of the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def check_score(playerscore, dealerscore):
    if playerscore == 0 or dealerscore == 0 or playerscore > 21:
        return True
    else:
        return False


def compare(user_score, computer_score):
    #Bug fix. If you and the computer are both over, you lose.
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)


for i in range(0, 2):
    user_card.append(deal_card())
    dealer_card.append(deal_card())

while not Game_ends:
    player_score = update_score(user_card)
    dealer_score = update_score(dealer_card)
    print(f" your cards : {user_card} , current score {player_score}")
    print(f"dealer first card {dealer_card[0]}")
    if player_score == 0 or dealer_score == 0 or player_score > 21:
        Game_ends = True
    else:
        user_should_dear = input("do want to draw another card 'y' or 'n' to end the game")
        if user_should_dear == "y":
            user_card.append(deal_card())
        else:
            Game_ends = True

while dealer_score != 0 and dealer_score < 17:
    dealer_card.append(deal_card())
    dealer_score = update_score(dealer_card)

print(f"   Your final hand: {user_card}, final score: {player_score}")
print(f"   Computer's final hand: {dealer_card}, final score: {dealer_score}")
print(compare(player_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
