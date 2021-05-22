from CharacterCard import CharacterCard

class Outlaw(CharacterCard):
    def __init__(self):
        image = None
        name = 'Outlaw'
        description = 'Kill the Sheriff'
        super().__init__(image, name, description)