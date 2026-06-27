from models.deck import Deck
from .player import Player
from .dealer import Dealer

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

        self.start_game()

    def start_game(self):
        self.distribute_starting_cards()
        
        print("Dealer Hands: ")
        print(self.dealer.hand.cards[0].get_card_string())

        print("Dealer Hands: ")
        print(self.player.hand.cards[0].get_card_string())

    def distribute_starting_cards(self):
        self.give_card(self.player)
        self.give_card(self.dealer)

    def give_card(self, player):
        player.hand.cards.append(self.deck.cards.pop()) 
