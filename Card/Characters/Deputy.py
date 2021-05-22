from CharacterCard import CharacterCard

class Deputy(CharacterCard):
    def __init__(self):
        image = None
        name = 'Deputy'
        description = 'Protect the Sheriff and kill any Outlaws'
        super().__init__(image, name, description)