from random import shuffle

from .card import Card


class Deck:
    def __init__(self):
        """ コンストラクタ """
        self.deck = []

    def get_deck(self) -> list:
        """ deck プロパティを返す """
        # todo: getter とか作るか
        return self.deck

    def init_deck(self) -> list:
        """ デッキを初期化 """
        self.card = Card()
        self.deck = self.card.create_new_deck()
        shuffle(self.deck)
        return self.deck

    def takeCard(self, count_of_card):
        """ カードを取られる """
        # todo: 非破壊的な処理が良さそう
        self.deck.pop(count_of_card)


if __name__ == '__main__':
    from pprint import pprint

    deck = Deck()
    pprint(deck.get_deck())
    
