import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Card import Card

class CharacterCard(Card):
    def __init__(self, image, name, description):
        super().__init__(image, name, description)
