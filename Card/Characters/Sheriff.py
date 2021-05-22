from CharacterCard import CharacterCard

class Deputy(CharacterCard):
    def __init__(self):
        image = None
        name = '보안관'
        description = '법과 질서를 수호하기 위해 무법자 전원과 배신자를 제거해야 합니다.'
        super().__init__(image, name, description)