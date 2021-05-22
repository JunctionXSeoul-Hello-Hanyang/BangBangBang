from . import ConsumptionCard

class Bang(ConsumptionCard):
    def __init__(self, image, name, description, number, trump_symbol):
        super().__init__(image, name, description, number, trump_symbol)

    def action(self, target_player_number, turn):
        turn.bang_turn(target_player_number)


