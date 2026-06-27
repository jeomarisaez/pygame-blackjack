from core.models.card import *

def main():
    card = Card(Ranks.JACK, Suits.HEARTS)
    print(card.get_card_string())

if __name__ == "__main__":
    main()