from .game import Game
from ui.ui import GameUI

class GameManager:
    def __init__(self):
        self.game = Game()
        self.user_interface = GameUI(self.game)
        self.user_interface.run()
        
    def start_game(self):
        game = Game()

