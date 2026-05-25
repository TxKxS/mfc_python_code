import globals



def prob_hiddenCard_10(D2, deck=[]):

    #let X be Dealer's hidden card
    
    if D2 in globals.tens_list:
        prob_X = (globals.tens +1)/ len(deck)
    else:
        prob_X = globals.tens/ len(deck)

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
    
