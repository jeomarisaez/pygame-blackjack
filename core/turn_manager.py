from enum import Enum

class Choice(Enum):
    HIT = 1
    STAND = 2

class TurnManager:
    def __init__(self, player_list):
        self.players = player_list
        self.turn_index = 0

    def start_turn(self):
        current_player = self.players[self.turn_index]
        print(f"\n--- It is {current_player.name}'s turn ---")
        return current_player

    def end_turn(self):
        self.turn_index += 1

        if self.turn_index >= len(self.players):
            self.turn_index = 0