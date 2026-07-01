import pygame
from .card import *
from .button import *
from .text import *

class GameUI:
    # colors
    BACKGROUND = (40, 40, 50)
    SLOT_COLOR = (100, 100, 120)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    BLUE = (50,50,255)

    CARD_SIZE = (60, 90)

    def __init__(self, screen):
        # dimensions
        self.screen = screen
        self.card_width, self.card_height = self.CARD_SIZE
        self.buttonUI = ButtonUI(self.screen)
        self.cardUI = CardUI(self.screen)
        self.textUI = TextUI(self.screen)

        # fonts
        self.card_font = pygame.font.SysFont("Arial", 30)
        self.corner_font = pygame.font.SysFont("Arial", 18)

    def draw(self, game):
        self.cardUI.draw_hand_slot(100)
        self.cardUI.draw_hand_slot(450)
        self.cardUI.draw_hand(game.player.hand.cards, 250, 450)
        self.cardUI.draw_hand(game.dealer.hand.cards, 250, 100)
        self.buttonUI.draw_button("hit", "HIT", 300, 550)
        self.buttonUI.draw_button("stand", "STAND", 500, 550)
        self.textUI.draw_counter(game.player.hand, 100, 450)
        self.textUI.draw_counter(game.dealer.hand, 100, 100)

        if game.game_over:
            self.textUI.draw_bust(game.current_player)



        
