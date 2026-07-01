from .ranks import Ranks

class Hand:
    def __init__(self):
        self.cards = []

    def get_first_card_value(self):
        match self.cards[0].rank:
                case Ranks.ACE:
                    value += 11
                    ace_count += 1
                case Ranks.TWO:
                    value += 2
                case Ranks.THREE:
                    value += 3
                case Ranks.FOUR:
                    value += 4
                case Ranks.FIVE:
                    value += 5
                case Ranks.SIX:
                    value += 6
                case Ranks.SEVEN:
                    value += 7
                case Ranks.EIGHT:
                    value += 8
                case Ranks.NINE:
                    value += 9
                case Ranks.TEN | Ranks.JACK | Ranks.QUEEN | Ranks.KING :
                    value += 10

    
    @property
    def get_value(self):
        value = 0
        ace_count = 0
        for card in self.cards:
            match card.rank:
                case Ranks.ACE:
                    value += 11
                    ace_count += 1
                case Ranks.TWO:
                    value += 2
                case Ranks.THREE:
                    value += 3
                case Ranks.FOUR:
                    value += 4
                case Ranks.FIVE:
                    value += 5
                case Ranks.SIX:
                    value += 6
                case Ranks.SEVEN:
                    value += 7
                case Ranks.EIGHT:
                    value += 8
                case Ranks.NINE:
                    value += 9
                case Ranks.TEN | Ranks.JACK | Ranks.QUEEN | Ranks.KING :
                    value += 10

        while value > 21 and ace_count > 0:
            value -= 10
            ace_count -= 1

        return value
