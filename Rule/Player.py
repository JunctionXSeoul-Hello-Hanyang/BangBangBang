from Rule import Field

class Player:
    def __init__(self, player_number, bullets, role, character, cards):
        self.player_number = player_number
        self.field = Field.Field(bullets, role, character)
        self.cards = cards


