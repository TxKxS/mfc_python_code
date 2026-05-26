Mathematical Foundation of Computing Python code formative

A Blackjack game where probability of getting a 10 and using having a 10 is given

Abstraction
This code is a simplification of the traditional Blackjack game played in casinos especially. This one is a 1 on 1 session where there is only 1 player who plays against the dealers using a 52 deck of poker cards. The program also calculates the probability of the dealer’s hidden card being a 10 and not being a 10. The code also calculates the probability of the next card being a 10 based on the factor whether the dealer’s card is a 10 or not.

Code SetUp- Introduction
The code follows the simple rules of Blackjack in casinos, the player against the dealer.

Assumptions:-
The player plays against the dealer
Only 1 player is playing, 1 on 1
The deck is a simple poker deck of 52 cards


Code Run:

A deck of 52 cards is created
Player and dealer are each given a random card twice
The visible cards are shown to the player
A first check is done to check for Blackjack, instant win/ lose
If there is no blackjack, the player is given the option to choose to hit (take 1 more)
The probability of the dealer having a 10 is shown to the player
The probability of the dealer not having a 10 is also shown
The probability of the next card being a 10 assuming that the dealer has a hidden 10 is given
The probability of the next card being a 10 given that the dealer’s hidden card is not a 10 is also given

In this report we will be looking at the math behind the code:

Code part:

import globals


def prob_hiddenCard_10(D2, deck=[]):


    #let X be Dealer's hidden card
   
    if D2 in globals.tens_list:
        #if dealer's hidden card is 10, need to add one to total count since we do not know as it is hidden
        prob_X = (globals.tens +1)/ (len(deck) +1)
    else:
        prob_X = globals.tens/ (len(deck) +1)


    prob_not_X =  1 - prob_X


    print("Probability that the dealer's hidden card is a 10 is:")
    print(prob_X)


    print("Probability that the dealer's hidden card is not a 10 is:")
    print(prob_not_X)


def prob_next_is10(D2, deck = []):


    #let Y be the next card
   
    print("Probability next card is a 10 given Dealer's hidden card is 10 is :  ")
    if D2 in globals.tens_list:
        prob_Y = globals.tens/ len(deck) #If we assume it is 10 and it really is a 10
        print(prob_Y)
    else:
        prob_Y = (globals.tens -1 )/ len(deck) #If we assume it is 10 and it is not a 10
        print(prob_Y)


    print("Probability next card is a 10 given Dealer's hidden card is not a 10 is :  ")
    if D2 in globals.tens_list:
        prob_Y = (globals.tens + 1)/ len(deck) #If we assume it is not a 10 and it is a 10
        print(prob_Y)
    else:
        prob_Y = (globals.tens)/ len(deck) #If we assume it is not a 10 and it is not a 10
        print(prob_Y)
   



Explanation:
An integer count ‘tens’ is used to store the number of cards which have a value of 10. The variable is stored in the globals file. This simplifies the algorithm and allows the probability to be calculated easier. 

First function ( prob_hiddenCard_10(D2, deck=[]) )

Prob of dealer’s card being a 10 it = ( tens / len(deck))
Let X be the value of the dealer’s hidden card

Since the dealer’s hidden card is drawn before the code with math runs, the dealer’s hidden card is needed to account for the extra card drawn. (ten+1)

The number of cards left is given by len(deck), so it needs to be incremented by 1 as the extra card has already been drawn. (len(deck) + 1) 

Now if the dealer’s hidden card was a 10, there is 1 ten or less from the count of ‘tens’ which is needed for the calculation, so we add one to the count of 10s. (tens +1)/ (len(deck) +1)
If the dealer’s hidden card is not a 10, then the number of tens left in the deck is the same as the current count of tens so no changes. (tens +1)/ (len(deck) +1)

Second function ( prob_next_is10(D2, deck = []) )

The next part of the code is to calculate the probability of the next card being a ten.
Now the issue is that 1 can has already been drawn but you do not know the value of it.
We therefore have 2 different possibilities, one where the card is a 10 and it is not 10.
In mathematics, we can use Bayes Theorem to calculate the probability of dependent issues but here for simplification, the code is responding to the situations and calculates the probability. 

Let Y be the value of the next card coming

So now, if the dealer’s hidden card is 10 and we assume it is a 10, the ‘tens’ count is right so we do not need to make any changes, so (tens) / len(deck)
If we assume it is 10 and it is not a 10, we will need to remove 1 from the ‘tens’ count to amend for the assumption we are making, so (tens - 1) / len(deck)

Then, if the dealer’s hidden card is not a 10 but we assume it is a 10, we need to remove the ten from the ‘tens’ count, so (tens -1) / len(deck)
Lastly, if we assume it is not a 10 and it really is not a 10, we do not need to make any change,  so (tens) / len(deck)



Repository Link:
Github link: https://github.com/TxKxS/mfc_python_code.git
