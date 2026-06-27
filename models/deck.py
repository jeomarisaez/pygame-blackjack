from .card import Card
from .ranks import Ranks
from .suits import Suits

class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck(self.cards)

    def create_deck(self, deck):
        for suit in Suits:
            for rank in Ranks:
                deck.append(Card(rank, suit))