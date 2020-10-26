# works perfectly: DO NOT MODIFY!
# requires "winnings" pre-defined

def bet_func(winnings):
    while True:
        try:
            bet = int(input(f"Your winnings are ${winnings}. Please place your bet: $"))
            if bet > 0 and bet < winnings:
                print(f"You bet ${bet}.")
                break;
            else:
                print(f"{bet} is not a valid bet.\nYou must place a bet within range of your winnings.")
        except ValueError:
            print("This is not a number. Try again.")
    return bet
