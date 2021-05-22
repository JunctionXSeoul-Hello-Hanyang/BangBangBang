from CharacterCard import CharacterCard

class Renegade(CharacterCard):
    def __init__(self):
        image = None
        name = 'Renegade'
        description = 'Be the last person standing'
        super().__init__(image, name, description)