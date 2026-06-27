class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def get_card_string(self):
        return f"{self.rank.value} of {self.suit.value}"
        