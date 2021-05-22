from . import EquipmentCard


class CharacterCard(EquipmentCard):
    def __init__(self, image, name, description):
        super().__init__(image, name, description)
