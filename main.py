from models.deck import Deck

def main():
    deck = Deck()
    for i in range(7): 
        print(deck.get_top_card().get_card_string())

if __name__ == "__main__":
    main()