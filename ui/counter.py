import pygame

class CounterUI:
    COUNTER_SIZE = (100, 50)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    BLUE = (50,50,255)

    def __init__(self, screen):
        self.screen = screen
        self.score_font = pygame.font.SysFont("Arial", 30)

    def draw_counter(self, hand, x, y):
        rect = pygame.Rect(0, 0, *self.COUNTER_SIZE)
        rect.center = (x, y)

        text_surf = self.score_font.render(str(hand.get_value), True, self.WHITE)

        self.screen.blit(text_surf, text_surf.get_rect(center=rect.center))