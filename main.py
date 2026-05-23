from globals import deck
import init_deck
import draw_card
import prob_math

def main():

    print("Welcome to the python code of TKS")

    deck = init_deck.create_deck()
    player_hand = []
    dealer_hand = []

    #print(globals.deck) for tesing purposes

    card = draw_card.draw_card(deck)
    player_hand.append(card)

    card = draw_card.draw_card(deck)
    dealer_hand.append(card)

    card = draw_card.draw_card(deck)
    player_hand.append(card)

    prob_math.prob_hiddenCard_10()
    

    #Deler's second card is drawn
    card = draw_card.draw_card(deck)
    dealer_hand.append(card)

    print("Player hand is :", player_hand)
    print("Dealer hand is :", dealer_hand[0], " #")

    input("Press enter to continue")
    print("Dealer's hand is: ", dealer_hand)
    print("Next card is : " , draw_card.draw_card(deck))

    '''
    card = draw_card.draw_card(deck)
    print(card)
    print(draw_card.draw_card(deck))

    print(deck)
    '''



if __name__ == "__main__" :
    main()


