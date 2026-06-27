from enum import Enum


class Suits(Enum):
    SPADES = "Spades"
    CLUBS = "Clubs"
    DIAMONDS = "Diamonds"
    HEARTS = "Hearts"

class Ranks(Enum):
    ACE = "Ace"
    TWO = "Two"
    THREE = "Three"
    FOUR = "Four"
    FIVE = "Five"
    SIX = "Six"
    SEVEN = "Seven"
    EIGHT = "Eight"
    NINE = "Nine"
    TEN = "Ten"
    JACK = "Jack"
    QUEEN = "Queen"
    KING = "King"

class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def get_card_string(self):
        return f"{self.rank.value} of {self.suit.value}"
        