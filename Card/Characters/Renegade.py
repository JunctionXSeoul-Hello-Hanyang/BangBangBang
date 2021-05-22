from CharacterCard import CharacterCard

class Renegade(CharacterCard):
    def __init__(self):
        image = None
        name = '배신자'
        description = '배신자의 목표는 새로운 보안관이 되기 위해 끝까지 혼자만 살아남는 것입니다.'
        super().__init__(image, name, description)