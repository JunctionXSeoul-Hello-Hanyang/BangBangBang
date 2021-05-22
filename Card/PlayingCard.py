from Card import Card


class PlayingCard(Card):
    def __init__(self, image, name, number, trump_symbol):
        super().__init__(image, name)
        self.number = number
        self.trump_symbol = trump_symbol

