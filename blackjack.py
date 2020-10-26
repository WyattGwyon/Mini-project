# Importing necessary librabries
# Recieved many TypeError: module object is not callable
# Solution: add "from"
import random
from bet_func import bet_func
from draw_funcs import num_func
from draw_funcs import suit_func
from draw_funcs import draw_func
from draw_funcs import discard_check_func
from dealer_deal_func import dealer_deal_func
from player_deal_func import player_deal_func
from sum_func import sum_func
from hit_func import hit_func
from compare_func import compare_func
from dealer_sum_func import dealer_sum_func


# Defining necessary variables
suits = ["clubs", "diamonds", "hearts", "spades"]
discard_lst = []
winnings = 1000
player_hand = []
dealer_hand = []
player_sum = 0
dealer_sum = 0


# We need to initiate the round every time we begin.

while True:
    try:
        start_game = input(f"Your winngins are ${winnings}. Would you like to start a game?")
        st_game = start_game.lower()


        # We check the answer given is valid
        if st_game == "y":
            print("Good luck!")
            break;
        elif st_game == "n":
            print(f"Thank You for playing! You won {winnings}.")
            quit()
        else:
            print(f"{st_game} is not a valid answer.")
            continue

    except:
        continue

        # We ask for the player's bet.
        bet = bet_func(winnings)
        winnings += bet


        # Now we need to deal the cards two to the player and dealer
        player_deal_func(player_hand, discard_lst, suits)
        dealer_deal_func(dealer_hand, discard_lst, suits)


        # We will sum the player's hand
        player_sum = sum_func(player_sum, player_hand)


        # Now we will ask player if he would like another card.
        hit = hit_func(discard_lst, player_hand, suits)

        if hit == "y":
            hit = hit_func(discard_lst, player_hand, suits)
            player_sum = sum_func(player_sum, player_hand)
            print(player_hand)
        else:
            pass


        # We will sum the dealer's cards
        dealer_sum_func(dealer_hand, discard_lst, dealer_sum)


        # Now we will compare player and dealer hands
        win = compare_func(player_sum, dealer_sum, winnings, bet)
    
