from . import GunCard

class Carabine(GunCard):
    def __init__(self, ):
        image = self.image
        description = ""
        number = ""
        trump_symbol = ""
        name = "Carabine"
        super().__init__(image, name, description, number, trump_symbol)