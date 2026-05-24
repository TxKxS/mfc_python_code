import random
import globals

def draw_card(deck):
    """
    Removes and returns one random card from the deck.
    """
    card = random.choice(deck)
    if card in globals.tens_list:
        globals.tens -= 1
        
    deck.remove(card)
    
    return card
