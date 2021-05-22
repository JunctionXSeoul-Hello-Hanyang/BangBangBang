from CharacterCard import CharacterCard

class Outlaw(CharacterCard):
    def __init__(self):
        image = None
        name = '무법자'
        description = '보안관을 제거하는 것이 목표이지만, 현상금에 눈이 멀어 거리낌 없이 다른 무법자를 제거하기도 합니다.'
        super().__init__(image, name, description)