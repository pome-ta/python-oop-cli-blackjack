class Card:
    """ 各カードの点数 """
    __CARD_SCORE = {
        'A': 1,  # Aは1点あるいは11点として点数が最大となる方で数える
        '2': 2,  # 2から9までは、書かれている数の点数
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,  # 10, J, Q, K は10点
        'J': 10,
        'Q': 10,
        'K': 10,
    }

    """ 各カードのマーク """
    __suits = [
        'スペード',
        'ハート',
        'ダイヤ',
        'クラブ',
    ]

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
