from points_calculator import points_calculator
import globals
import init_deck
import draw_card
import prob_math

def main():

    print("Welcome to the blackjack code of TKS")

    deck = init_deck.create_deck()
    player_hand = []
    dealer_hand = []

    #print(globals.deck) for tesing purposes

    #Player first card is drawn
    card = draw_card.draw_card(deck)
    player_hand.append(card)

    #Dealer's first card is drawn
    card = draw_card.draw_card(deck)
    dealer_hand.append(card)

    #Player second card is drawn
    card = draw_card.draw_card(deck)
    player_hand.append(card)

    #Dealer's second card is drawn
    card = draw_card.draw_card(deck)
    dealer_hand.append(card)

    print("Dealer hand is :", dealer_hand[0], " #")
    print("Player hand is :", player_hand)

    #prob_math.prob_hiddenCard_10(dealer_hand[1], deck)

    #checking for blackjack
    
    if points_calculator(player_hand) == 21  and points_calculator(dealer_hand) != 21 :
        print("BLACKJACK")
        print("Instant WIN")
    else:
        if points_calculator(player_hand) != 21 and points_calculator(dealer_hand == 21):
            print("Dealer Blackjack")
            print("Player lose")
        else:
            if points_calculator(player_hand) == 21 and points_calculator(dealer_hand == 21):
                print("Both player and dealer Blackjack")
                print("No winner. Push")

    while True:

        prob_math.prob_hiddenCard_10(dealer_hand[1], deck)
        prob_math.prob_next_is10(dealer_hand[1], deck)
        print()

        print("Will player draw 1 more card?")
        choice = str(input("Enter 1 for Yes and 2 for no : "))
        if choice == "1":
            player_hand.append(draw_card.draw_card(deck))
            print("Player hand is :", player_hand)
            print("Dealer hand is : [", dealer_hand[0], ", #]")

            continue
        elif choice == "2":
            break

    input("Press enter to continue \n")
    print("Dealer's hand is: ", dealer_hand)
    print("Player hand is: ", player_hand)

    player_points = points_calculator(player_hand)
    dealer_points = points_calculator(dealer_hand)

    
    print("You have",player_points , " points")
    print("Dealer has ",dealer_points, " points")

    if player_points > 21:
        print("Burst. Player loses")
    else:
            while dealer_points < 17:
                print("Since dealer has less than 17 points, they need to draw 1 more")
                card = draw_card.draw_card(deck)
                dealer_hand.append(card)
                dealer_points = points_calculator(dealer_hand)

            print("Dealer's hand is: ", dealer_hand)
            print("Player hand is: ", player_hand)

            print("You have",player_points , " points")
            print("Dealer has ",dealer_points, " points")

            if dealer_points > 21:
                 print("Dealer bursted player wins.")
            else:
                if player_points > dealer_points:
                    print("Player has more points, player wins.")
                elif dealer_points > player_points:
                    print("Dealer has more points. Dealer wins.")
                else:
                    print("Same points. Push")

    print()
    print("Tens left ", globals.tens )
    print("Cards left: ", len(deck))
    print("Next card was : " , draw_card.draw_card(deck))
    
    #print(deck) #testing purposes
    



if __name__ == "__main__" :
    main()


