from draw_funcs import discard_check_func

#This function needs to hide one card and show the other
def dealer_deal_func(dealer_hand, discard_lst,suits):
    while True:
        if len(dealer_hand) < 2:
            discard_check_func(discard_lst, dealer_hand, suits)
        else:
            break
    print("Dealer hand:",dealer_hand[0])
