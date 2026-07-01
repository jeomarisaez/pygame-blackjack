from .game import Game
from ui.game_ui import GameUI
import os
import pygame

class GameManager:
    BACKGROUND = (40, 40, 50)

    def __init__(self):
        pygame.init()

        icon = pygame.image.load(os.path.join("assets", "penguin.png"))
        pygame.display.set_icon(icon)

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Penguin's Blackjack")

        self.clock = pygame.time.Clock()
        self.running = True

        self.game = Game()
        self.game.start()   
        self.game_ui = GameUI(self.screen)

        self.run()

    def run(self):
        surface = self.screen

        while self.running:
            self.handle_inputs()

            self.screen.fill(self.BACKGROUND)

            self.game_ui.draw(self.game)
            
            # # updates screen so that all blipped elements show
            pygame.display.flip()

        pygame.quit()

    def handle_inputs(self):
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if self.game_ui.buttonUI.mouse_inside("new_game", event.pos):
                        print(self.game.game_over)
                        if self.game.game_over:
                            self.restart_game()
                            print("new game pressed")

                if self.game.current_player == self.game.player:
                    if self.game_ui.buttonUI.mouse_inside("hit", event.pos):
                        self.game.hit(self.game.current_player)
                        print("hit pressed")
                    if self.game_ui.buttonUI.mouse_inside("stand", event.pos):
                        self.game.stand(self.game.current_player)
                        print("stand pressed")
                    

            if event.type == pygame.KEYDOWN:
                if self.game.current_player == self.game.player:
                    if event.key == pygame.K_1:
                        self.game.hit(self.game.current_player)
                        print("hit pressed")
                    if event.key == pygame.K_2:
                        self.game.stand(self.game.current_player)
                        print("stand pressed")

        # hover handling
        if self.game_ui.buttonUI.mouse_inside("hit", mouse_pos):
            self.game_ui.buttonUI.hovered_button = "hit"
        elif self.game_ui.buttonUI.mouse_inside("stand", mouse_pos):
            self.game_ui.buttonUI.hovered_button = "stand"
        else:
            self.game_ui.buttonUI.hovered_button = None

    def restart_game(self):
        self.game = Game()
        self.game.start()




