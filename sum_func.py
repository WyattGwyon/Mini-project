

def sum_func(sum, hand):
    for card in hand:
        if card[0] == "J" or card[0] == "Q" or card[0] == "K":
            sum += 10
        elif card[0] == "A":
            while True:
                try:
                    ace_value = int(input(f"Choose a value for Ace (1 or 11)?"))
                    if ace_value == 1 or ace_value == 11:
                        sum += ace_value
                        break
                    else:
                        print(f"{ace_value} is not a valid response.")
                except ValueError:
                    print("This is not a number. Try again.")
        else:
            sum += card[0]

    print(f"Your cards add up to {sum}.")
    if sum > 21:
        print("Bust! Dealer wins")

    return sum
