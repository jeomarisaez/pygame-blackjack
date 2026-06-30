import pygame
import sys
class ButtonUI:
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

        # fonts
        self.card_font = pygame.font.SysFont("Arial", 30)
        self.corner_font = pygame.font.SysFont("Arial", 18)

    def draw_button(self, text, x, y, width=100, height=50):
        surface = self.screen
        btn_x_offset = width * 0.5
        btn_y_offset = height * 0.5


        rect = pygame.Rect(x - btn_x_offset, y - btn_y_offset, width, height)

        pygame.draw.rect(surface, self.BLUE, rect, border_radius=12)  
        pygame.draw.rect(surface, self.BLACK, rect, 2, border_radius=12)  

        text_surf = self.card_font.render(text, True, self.WHITE)
        text_rect = text_surf.get_rect(center=rect.center)

        surface.blit(text_surf, text_rect)



        
