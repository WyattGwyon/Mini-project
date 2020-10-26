import random


def num_func():
    rand_num = random.choice(range(1,13))
    if rand_num == 1:
        rand_num = "A"
    elif rand_num == 11:
        rand_num = "J"
    elif rand_num == 12:
        rand_num = "Q"
    elif rand_num == 13:
        rand_num = "K"
    return rand_num

def suit_func(suits):
    rand_suit = random.choice(suits)
    return rand_suit

# This functions works with number() and suit(suits) as arguments
# and returns an actual card
def draw_func(num_func, suit_func):
    card = num_func, suit_func
    return card


# This function draws, checks, and places cards into hands of dealer and player
# It is the most complex of the draw functions and
# It will be the function we call to draw cards at any time in the game
def discard_check_func(discard_lst, hand, suits):
    card = draw_func(num_func(),suit_func(suits))
    if len(discard_lst) == 52:
        discard_lst.clear()
        card = draw_func(num_func(),suit_func(suits))
    elif card in discard_lst:
        card = draw_func(num_func(),suit_func(suits))
    else:
        pass
    hand.append(card)
    discard_lst.append(card)
