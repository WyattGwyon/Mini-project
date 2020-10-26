

def compare_func(player_sum, dealer_sum, winnings, bet):
    if player_sum <= dealer_sum:
        print(f"Dealer wins. your total is {winnings}")
    elif player_sum > dealer_sum:
        winnings += bet * 2
        print(f"You win, your total is {winnings}")
    
    return winnings
