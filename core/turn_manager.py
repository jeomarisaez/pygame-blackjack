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

    def ask_choice(self):
        while True:
            choice = input("Type '1' to hit, '2' to stand: ").strip()
            
            match choice:
                case "1":
                    return Choice.HIT
                case "2":
                    return Choice.STAND
                case _:
                    print("Invalid input. Please try again.")