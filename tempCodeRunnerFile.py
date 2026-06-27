from models.deck import Deck
import pygame

def main():
    deck = Deck()
    deck.create_deck()
    print(deck.deck_list)

if __name__ == "__main__":
    main()