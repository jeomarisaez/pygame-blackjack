import pygame
import sys

class GameUI:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygame UI Manager")
        self.clock = pygame.time.Clock()
        self.running = True

        # dimensions
        self.card_width = 60
        self.card_height = 90
        
        self.screen_width = self.screen.get_width()   
        self.screen_height = self.screen.get_height()  
        
        self.card_x_offset = self.card_width / 2
        self.card_y_offset = self.card_height / 2

        self.screen_center_x = self.screen_width * 0.5
        self.screen_center_y = self.screen_height * 0.5

        
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.screen.fill((40, 40, 50))
            # creates cards
            self.display_hand_slot()
            self.show_card("A", 1, (self.screen_center_x - self.card_x_offset) - 50, self.screen_center_y * 1.5 - self.card_y_offset) 
            self.show_card("B", 2, (self.screen_center_x - self.card_x_offset) + 50, self.screen_center_y * 1.5 - self.card_y_offset)
            # updates screen so that all blipped elements show
            pygame.display.flip()

        pygame.quit()
        # sys.exit()

    def display_card(self, suit, rank, x, y, width=60, height=90):

        surface = self.screen

        rect = pygame.Rect(x, y, width, height)

        pygame.draw.rect(surface, (224, 224, 224), rect, border_radius=12)  

    def display_hand_slot(self, width=500, height=120):
        slot_x_offset = width / 2
        slot_y_offset = height / 2

        surface = self.screen

        rect = pygame.Rect(self.screen_center_x - slot_x_offset, self.screen_center_y * 1.5 - slot_y_offset, width, height)
        # draw the bg filled card slots
        pygame.draw.rect(surface, (100, 100, 120), rect, border_radius=12)  

        
    def show_card(self, letter, number, x, y, width=60, height=90):

        surface = self.screen

        rect = pygame.Rect(x, y, width, height)
        # draw the bg filled card
        pygame.draw.rect(surface, (255, 255, 255), rect, border_radius=12)  
        # draw the outline uptop
        pygame.draw.rect(surface, (0, 0, 0), rect, 2, border_radius=12)   

        # makes a font that's scaled to card height for the suit
        font = pygame.font.SysFont("Arial", height // 3)
        # render letter as surface
        letter_surf = font.render(letter, True, (255, 0, 0))
        # position it centered
        letter_rect = letter_surf.get_rect(centerx=rect.centerx, centery=rect.centery)
        # stamp the letter onto screen
        surface.blit(letter_surf, letter_rect)

        # makes a font that's scaled to card height for the rank
        small_font = pygame.font.SysFont("Arial", height // 5)
        # render number as surface
        num_surf = small_font.render(str(number), True, (255, 0, 0))
        # position it on the bottom right
        num_rect_top_left = num_surf.get_rect(left=rect.left + 6, top=rect.top + 6)
        # position it on the top left
        num_rect_bottom_right = num_surf.get_rect(right=rect.right - 6, bottom=rect.bottom - 6)
        
        # stamp number onto screen
        surface.blit(num_surf, num_rect_bottom_right)
        surface.blit(num_surf, num_rect_top_left)

        
