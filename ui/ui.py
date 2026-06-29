import pygame
import sys
class GameUI:
    # colors
    SLOT_COLOR = (100, 100, 120)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)

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

    def run(self):
        surface = self.screen

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            
            self.screen.fill(self.BACKGROUND)
            # creates cards
            self.draw_hand_slot(self.screen_center_y * 1.5)
            self.draw_hand_slot(self.screen_center_y * 0.5)
            self.draw_card("A", 1, (self.screen.center_x - self.card_x_offset) - 50, self.screen_center_y * 1.5 - self.card_y_offset) 
            self.draw_card("B", 2, (self.screen.center_x - self.card_x_offset) + 50, self.screen_center_y * 1.5 - self.card_y_offset)
            # updates screen so that all blipped elements show
            pygame.display.flip()
        pygame.quit()
        # sys.exit()

    def draw_hand_slot(self, y, width=500, height=120):
        slot_x_offset = width / 2
        slot_y_offset = height / 2

        surface = self.screen

        rect = pygame.Rect(self.screen_center_x - slot_x_offset, y - slot_y_offset, width, height)
        # draw the bg filled card slots
        pygame.draw.rect(surface, self.SLOT_COLOR, rect, border_radius=12)  
        
    def draw_card(self, letter, number, x, y, width=60, height=90):
        surface = self.screen

        rect = pygame.Rect(x, y, width, height)
        # draw the bg filled card
        pygame.draw.rect(surface, self.WHITE, rect, border_radius=12)  
        # draw the outline uptop
        pygame.draw.rect(surface, self.BLACK, rect, 2, border_radius=12)   

        # makes a font that's scaled to card height for the suit
        font = pygame.font.SysFont("Arial", height // 3)
        # render letter as surface
        letter_surf = self.card_font.render(letter, True, self.RED)
        # position it centered
        letter_rect = letter_surf.get_rect(centerx=rect.centerx, centery=rect.centery)
        # stamp the letter onto screen
        surface.blit(letter_surf, letter_rect)

        # makes a font that's scaled to card height for the rank
        small_font = pygame.font.SysFont("Arial", height // 5)
        # render number as surface
        num_surf = self.corner_font.render(str(number), True, self.RED)
        # position it on the bottom right
        num_rect_top_left = num_surf.get_rect(left=rect.left + 6, top=rect.top + 6)
        # position it on the top left
        num_rect_bottom_right = num_surf.get_rect(right=rect.right - 6, bottom=rect.bottom - 6)
        
        # stamp number onto screen
        surface.blit(num_surf, num_rect_bottom_right)
        surface.blit(num_surf, num_rect_top_left)
        

    def draw_button():
        pass

        
