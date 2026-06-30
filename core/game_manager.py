from .game import Game
from ui.game_ui import GameUI
import pygame
import sys

class GameManager:
    BACKGROUND = (40, 40, 50)

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Card Game")

        self.clock = pygame.time.Clock()
        self.running = True

        self.game = Game()
        self.game_ui = GameUI(self.screen)

        self.run()


    def run(self):
        surface = self.screen

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.game.current_player == self.game.player:
                        if self.game_ui.buttonUI.clicked("hit", event.pos):
                            self.game.hit(self.game.current_player)
                            print("hit pressed")
                        if self.game_ui.buttonUI.clicked("stand", event.pos):
                            self.game.stand(self.game.current_player)
                            print("stand pressed")


            self.screen.fill(self.BACKGROUND)

            self.game_ui.draw(self.game)


            
            # self.game_ui.draw_hand_slot(self.game_ui.screen_center_y * 1.5)
            # self.game_ui.draw_hand_slot(self.game_ui.screen_center_y * 0.5)
            # self.game_ui.draw_card("A", 1, (self.game_ui.screen_center_x - self.game_ui.card_x_offset) - 50, self.game_ui.screen_center_y * 1.5 - self.game_ui.card_y_offset) 
            # self.game_ui.draw_card("B", 2, (self.game_ui.screen_center_x - self.game_ui.card_x_offset) + 50, self.game_ui.screen_center_y * 1.5 - self.game_ui.card_y_offset)
            # # updates screen so that all blipped elements show
            pygame.display.flip()

        pygame.quit()
        # sys.exit()

