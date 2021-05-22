from . import Card

class PlayingCard(Card):
    def __init__(self, image, name, description, number, trump_symbol):
        super().__init__(image, name, description)
        self.number = number
        self.trump_symbol = trump_symbol

