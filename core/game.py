from models.deck import Deck
from .player import Player
from .dealer import Dealer
from .turn_manager import *

class Game:
    def __init__(self):
        self.game_over = False

        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

        self.player_list = [self.player, self.dealer]
        self.turn_manager = TurnManager(self.player_list)

        self.current_player = None
        self.player_turn_active = False

        self.set_up_game()
        self.play_turn()

    def set_up_game(self):
        self.distribute_starting_cards()

        print("Dealer Hand: ")
        self.print_hands(self.dealer.hand.cards)

        print("Player Hand: ")
        self.show_hand_value(self.player.hand)
        self.print_hands(self.player.hand.cards)
    
    def play_turn(self):
        self.current_player = self.turn_manager.start_turn()

        # dealer logic handler
        if isinstance(self.current_player, Dealer):
            self.handle_dealer_turn(self.current_player)
            return
        
        self.player_turn_active = True
        
    
    def handle_dealer_turn(self, dealer):
        dealer.hand.cards[1].hidden = False

        print("Dealer reveals hand:")
        self.print_hands(dealer.hand.cards)

        # basic dealer rules for optimal choices
        while dealer.hand.get_value < 17:
            print("Dealer hits...")
            self.hit(dealer)
            self.print_hands(dealer.hand.cards)

        if dealer.hand.get_value > 21:
            print("Dealer busted!")

        self.check_win()
            
        self.game_over = True

    def distribute_starting_cards(self):
        for i in range(2):
            self.give_card(self.player)
            self.give_card(self.dealer)
            if i > 0:
                self.dealer.hand.cards[i].hidden = True
        
    def give_card(self, player):
        player.hand.cards.append(self.deck.cards.pop()) 

    def print_hands(self, cards):
        for card in cards:
            if card.hidden == True:
                print(f"\tHidden")
            else:
                print(f"\t{card.get_card_string()}")

    def show_hand_value(self, hand):
        print(f"Value: {hand.get_value}")
        
    def hit(self, player):
        self.give_card(player)

    def stand(self, player):
        print(f"{player.name} decides to stand.")

    def check_win(self):
        highest_score = 0
        for player in self.player_list:
            if highest_score < player.hand.get_value:
                current_winner = player.name
                highest_score = player.hand.get_value
        return current_winner

