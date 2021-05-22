from CharacterCard import CharacterCard

class Deputy(CharacterCard):
    def __init__(self):
        image = None
        name = 'Sheriff'
        description = 'Kill all Outlaws and the Renegade'
        super().__init__(image, name, description)