class Card:
    __CARD_SCORE = {
        'A': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
    }

    __suits = ['スペード', 'ハート', 'ダイヤ', 'クラブ', ]

    def create_new_deck(self) -> list:
        # deck = []
        # for suit in self.__suits:
        #     for score, num in self.__CARD_SCORE.items():
        #         deck.append({'suit': suit, 'num': num, 'score': score})
        # return deck
        deck = [{
            'suit': suit,
            'num': num,
            'score': score,
        } for score, num in self.__CARD_SCORE.items() for suit in self.__suits]
        return deck


if __name__ == '__main__':
    from pprint import pprint

    card = Card()
    pprint(card.create_new_deck())
