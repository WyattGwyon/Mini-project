from draw_funcs import discard_check_func

# I don't know if this really works yet

def hit_func(discard_lst, player_hand, suits):

    while True:
        try:
            hit_inp = input("Would you like to hit (y/n)?")
            hit = hit_inp.lower()
            if hit == "y":
                discard_check_func(discard_lst, player_hand, suits)
                print("Your hand:", player_hand)
                break;
            elif hit == "n":
                break;
            else:
                print(f"{hit} is not a valid response")
        except:
            continue
    return hit
