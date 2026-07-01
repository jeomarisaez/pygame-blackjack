import pygame
import sys

class CardUI:
    # colors
    BACKGROUND = (40, 40, 50)
    SLOT_COLOR = (100, 100, 120)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    BLUE = (50,50,255)


    SLOT_SIZE = (500, 120)
    CARD_SIZE = (60, 90)

    def __init__(self, screen):
        # dimensions
        self.screen = screen
        self.card_width, self.card_height = self.CARD_SIZE

        # self.screen_width = self.screen.get_width()   
        # self.screen_height = self.screen.get_height()  
        
        # self.card_x_offset = self.card_width / 2
        # self.card_y_offset = self.card_height / 2

        # self.screen_center_x = self.screen_width * 0.5
        # self.screen_center_y = self.screen_height * 0.5

        # fonts
        self.card_font = pygame.font.SysFont("Arial", 30)
        self.corner_font = pygame.font.SysFont("Arial", 18)


    def draw_hand(self, cards, x, y):
        for card in cards:
            if card.hidden:
                self.draw_card_back(x, y)
            else:
                self.draw_card(card, x, y)
            x += 70


    def draw_hand_slot(self, y):
        screen_rect = self.screen.get_rect()

        rect = pygame.Rect(0, 0, *self.SLOT_SIZE)
        rect.center = (screen_rect.centerx, y)

        pygame.draw.rect(
            self.screen,
            self.SLOT_COLOR,
            rect,
            border_radius=12
        )
        
    def draw_card(self, card, x, y):
        # pygame does the center positioning itself
        rect = pygame.Rect(0, 0, *self.CARD_SIZE)
        rect.center = (x, y)

        pygame.draw.rect(self.screen, self.WHITE, rect, border_radius=12)  
        pygame.draw.rect(self.screen, self.BLACK, rect, 2, border_radius=12)  

        suit = card.suit
        rank = card.rank 


        if suit in [suit.HEARTS, suit.DIAMONDS]:
            color = self.RED
        else:
            color = self.BLACK
        
        suit_text = self.card_font.render(suit.value, True, color)

        self.screen.blit(suit_text, suit_text.get_rect(center=rect.center))
        
        rank_text = self.corner_font.render(rank.value, True, color)

        self.screen.blit(rank_text, rank_text.get_rect(left=rect.left + 6, top=rect.top + 6))
        self.screen.blit(rank_text, rank_text.get_rect(right=rect.right - 6, bottom=rect.bottom - 6))


    def draw_card_back(self, x, y):

        rect = pygame.Rect(0, 0, *self.CARD_SIZE)
        rect.center = (x, y)

        pygame.draw.rect(self.screen, self.RED, rect, border_radius=12)  
        pygame.draw.rect(self.screen, self.BLACK, rect, 2, border_radius=12)  

 



        
