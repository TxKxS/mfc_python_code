import globals
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

    #Deler's second card is drawn
    card = draw_card.draw_card(deck)
    dealer_hand.append(card)

    print("Player hand is :", player_hand)
    print("Dealer hand is :", dealer_hand[0], " #")

    prob_math.prob_hiddenCard_10()

    while True:
        print("Will player draw 1 more card?")
        choice = str(input("Enter 1 for Yes and 2 for no : "))
        if choice == "1":
            player_hand.append(draw_card.draw_card(deck))
            print("Player hand is :", player_hand)
            print("Dealer hand is : [", dealer_hand[0], ", #]")
            continue
        elif choice == "2":
            break




    input("Press enter to continue")
    print("Dealer's hand is: ", dealer_hand)

    print("Tens left ", globals.tens )
    
    print("Next card is : " , draw_card.draw_card(deck))
    
    print(deck)
    



if __name__ == "__main__" :
    main()


