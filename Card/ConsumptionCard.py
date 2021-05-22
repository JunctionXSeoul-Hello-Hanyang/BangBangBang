from Card import PlayingCard


class EquipmentCard(PlayingCard):
    def __init__(self, image, name, number, trump_symbol):
        super().__init__(image, name, number, trump_symbol)

