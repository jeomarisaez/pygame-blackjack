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
        self.result_text = ""
        self.winner = ""

    def start(self):
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

        while dealer.hand.get_value < 17:
            print("Dealer hits...")
            self.hit(dealer)
            self.print_hands(dealer.hand.cards)

        if dealer.hand.get_value > 21:
            self.result_text = f"{dealer.name} busted! Player wins!"
        elif self.check_win() == "Tie":
            self.result_text = "Tie"
        else:
            self.result_text = f"{self.check_win()} wins!"

        self.end_game()

    def end_game(self):
        self.game_over = True
        self.player_turn_active = False
        self.winner = self.check_win()

        if self.result_text == "":
            self.result_text = f"{self.winner} wins!"

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

        print(f"{player.name}'s hand:")
        self.show_hand_value(player.hand)
        self.print_hands(player.hand.cards)

        if player.hand.get_value > 21:
            self.result_text = f"{player.name} busted!"

            if isinstance(player, Player):
                self.result_text += " Dealer wins!"
            else:
                self.result_text += " Player wins!"

            self.end_game()


    def stand(self, player):
        print(f"{player.name} decides to stand.")

        self.player_turn_active = False

        self.turn_manager.end_turn()

        self.play_turn()

    def check_win(self):
        player_score = self.player.hand.get_value
        dealer_score = self.dealer.hand.get_value

        if player_score > 21:
            return self.dealer.name

        if dealer_score > 21:
            return self.player.name

        if player_score > dealer_score:
            return self.player.name

        if dealer_score > player_score:
            return self.dealer.name

        return "Tie"

