from Rule import Field

class Player:
    def __init__(self, player_number, bullets, role, character, cards):
        self.player_number = 'Player' + player_number
        self.field = Field(bullets, role, character)
        self.cards = cards


