from draw_funcs import discard_check_func
import random

def player_deal_func(player_hand, discard_lst, suits):
    while True:
        if len(player_hand) < 2:
            discard_check_func(discard_lst, player_hand, suits)
        else:
            break
    print("Your hand:",player_hand)
