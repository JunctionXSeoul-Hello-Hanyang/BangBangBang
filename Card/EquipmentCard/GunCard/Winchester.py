from . import GunCard

class Winchester(GunCard):
    def __init__(self, image, name, description, number, trump_symbol):
        super().__init__(image, name, description, number, trump_symbol)