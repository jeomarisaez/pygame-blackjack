from .game import Game
from ui.ui import GameUI
import pygame

class GameManager:
    BACKGROUND = (40, 40, 50)

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Card Game")

        self.clock = pygame.time.Clock()
        self.running = True

        self.ui = GameUI(self.screen)
        self.run()

        # self.game = Game()
        # self.user_interface = GameUI(self.game)
        # self.user_interface.run()

    def run(self):
        surface = self.screen

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(self.BACKGROUND)
            
            self.ui.draw_hand_slot(self.ui.screen_center_y * 1.5)
            self.ui.draw_hand_slot(self.ui.screen_center_y * 0.5)
            self.ui.draw_card("A", 1, (self.ui.screen_center_x - self.ui.card_x_offset) - 50, self.ui.screen_center_y * 1.5 - self.ui.card_y_offset) 
            self.ui.draw_card("B", 2, (self.ui.screen_center_x - self.ui.card_x_offset) + 50, self.ui.screen_center_y * 1.5 - self.ui.card_y_offset)
            # updates screen so that all blipped elements show
            pygame.display.flip()
        pygame.quit()
        # sys.exit()
        
    def start_game(self):
        game = Game()

