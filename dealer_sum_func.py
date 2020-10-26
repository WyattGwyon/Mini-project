from draw_funcs import discard_check_func
from sum_func import sum_func

def dealer_sum_func(dealer_hand, discard_lst, dealer_sum):
    for card in dealer_hand:
        if card[0] == "J" or card[0] == "Q" or card[0] == "K":
            dealer_sum += 10
        elif card[0] == "A":
            dealer_sum += 11
        else:
            dealer_sum += card[0]
    if dealer_sum > 17:
        discard_check_func(discard_lst, dealer_hand,suits)
    else:
        pass
