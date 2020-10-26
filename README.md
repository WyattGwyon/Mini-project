# BlackJack, or 21

This is a game of BlackJack.
The objective is to get a sum of 21 from the cards in your hand.
If you go over, you lose.
The highest hand without going over 21 wins.

We need to initiate the game with the player only acepting certain input. Here, we need a yes or no. This question will repeat at the end of the hand to continue the game if the player wants to keep playing or they can stop and walk away with their earnings. 

If the player wants to continue, they must make a bet. They can only make a bet within the limit of the amount of money they have. No other input will be accepted.

Dealing the cards out is a complex series of steps to organize the deck so that each card that is drawn is unique and has not been previously drawn. The next step is to insure that when the deck is full, it gets shuffled. In this case we simply empty the deck.

Now, the player recieves two cards they can see and the dealer receives two cards but only one is visible. They can see the sum of their cards and are asked if they want to hit or not. If they hit they will recieve an update of their hand and sum. They can continue to hit until they bust, or go over 21.

If they player is still in the game, the dealer will draw or not and show his hand. The player's winnings will reflect the outcome of the hand.

The player can choose to continue or walk away with their winnings.

If you want to try...
Open the blackjack.py in your terminal and start playing.
