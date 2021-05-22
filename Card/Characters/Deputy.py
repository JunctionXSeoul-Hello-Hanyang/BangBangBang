from CharacterCard import CharacterCard

class Deputy(CharacterCard):
    def __init__(self):
        image = None
        name = '부관'
        description = '보안관이 목표를 이룰 수 있도록 모든 것을 걸고 보안관을 돕고 보호합니다.'
        super().__init__(image, name, description)