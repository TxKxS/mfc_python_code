import random

def draw_card(deck):
    """
    Removes and returns one random card from the deck.
    """
    card = random.choice(deck)
    deck.remove(card)
    
    return card
