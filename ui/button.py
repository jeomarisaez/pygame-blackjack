import pygame
import sys
class ButtonUI:
    # colors
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    BLUE = (50,50,255)

    BUTTON_SIZE = (100, 50)

    def __init__(self, screen):
        # dimensions
        self.screen = screen
        self.buttons = {}

        # fonts
        self.font = pygame.font.SysFont("Arial", 30)

    def draw_button(self, name, text, x, y):
        rect = pygame.Rect(0, 0, *self.BUTTON_SIZE)
        rect.center = (x, y)

        self.buttons[name] = rect

        pygame.draw.rect(self.screen, self.BLUE, rect, border_radius=12)  
        pygame.draw.rect(self.screen, self.BLACK, rect, 2, border_radius=12)  

        text_surf = self.font.render(text, True, self.WHITE)

        self.screen.blit(text_surf, text_surf.get_rect(center=rect.center))

    def clicked(self, name, pos):
        return self.buttons[name].collidepoint(pos)



        
