from . import GunCard

class Colt45(GunCard):
    def __init__(self, image, name, description, number, trump_symbol):
        image = self.image
        name = "Colt45"
        description = "Default Weapon"
        number = 0
        trump_symbol = ""
        super().__init__(image, name, description, number, trump_symbol)