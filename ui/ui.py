import pygame
import sys
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

        self.screen_width = self.screen.get_width()   
        self.screen_height = self.screen.get_height()  
        
        self.card_x_offset = self.card_width / 2
        self.card_y_offset = self.card_height / 2

        self.screen_center_x = self.screen_width * 0.5
        self.screen_center_y = self.screen_height * 0.5

        # fonts
        self.card_font = pygame.font.SysFont("Arial", 30)
        self.corner_font = pygame.font.SysFont("Arial", 18)

    def draw(self, game):
        self.draw_hand_slot(100)
        self.draw_hand_slot(450)
        self.draw_player_hand(game.player.hand.cards)
        self.draw_dealer_hand(game.dealer.hand.cards)


    def draw_player_hand(self, cards):

        x = 250
        y = 450

        for card in cards:

            self.draw_card(card, x - self.card_x_offset, y - self.card_y_offset)
            x += 70

    def draw_dealer_hand(self, cards):
        x = 250
        y = 100

        for card in cards:
            if card.hidden:
                self.draw_card_back(x - self.card_x_offset, y - self.card_y_offset)
            else:
                self.draw_card(card, x - self.card_x_offset, y - self.card_y_offset)

            x += 70


    def draw_hand_slot(self, y, width=500, height=120):
        slot_x_offset = width / 2
        slot_y_offset = height / 2

        surface = self.screen

        rect = pygame.Rect(self.screen_center_x - slot_x_offset, y - slot_y_offset, width, height)
        # draw the bg filled card slots
        pygame.draw.rect(surface, self.SLOT_COLOR, rect, border_radius=12)  
        
    def draw_card(self, card, x, y, width=60, height=90):
        surface = self.screen

        rect = pygame.Rect(x, y, width, height)

        pygame.draw.rect(surface, self.WHITE, rect, border_radius=12)  
        pygame.draw.rect(surface, self.BLACK, rect, 2, border_radius=12)  

        suit = card.suit
        rank = card.rank 


        if suit in [suit.HEARTS, suit.DIAMONDS]:
            color = self.RED
        else:
            color = self.BLACK
        
        suit_surf = self.card_font.render(suit.value, True, color)
        suit_rect = suit_surf.get_rect(center=rect.center)

        surface.blit(suit_surf, suit_rect)
        
        rank_surf = self.corner_font.render(rank.value, True, color)

        top_left = rank_surf.get_rect(left=rect.left + 6, top=rect.top + 6)
        bottom_right = rank_surf.get_rect(right=rect.right - 6, bottom=rect.bottom - 6)
        
        # stamp rank onto screen
        surface.blit(rank_surf, bottom_right)
        surface.blit(rank_surf, top_left)

    def draw_card_back(self, x, y, width=60, height=90):
        surface = self.screen

        rect = pygame.Rect(x, y, width, height)

        pygame.draw.rect(surface, self.RED, rect, border_radius=12)  
        pygame.draw.rect(surface, self.BLACK, rect, 2, border_radius=12)  

    def draw_button(self, text, x, y, width=100, height=50):
        surface = self.screen

        rect = pygame.Rect(x, y, width, height)

        pygame.draw.rect(surface, self.BLUE, rect, border_radius=12)  
        pygame.draw.rect(surface, self.BLACK, rect, 2, border_radius=12)  

        text_surf = self.card_font.render(text, True, self.WHITE)
        text_rect = text_surf.get_rect(center=rect.center)

        surface.blit(text_surf, text_rect)



        
