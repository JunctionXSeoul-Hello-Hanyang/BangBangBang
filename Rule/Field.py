import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Card import Card

class Field:
    def __init__(self, bullets, role, character):
        self.bullets = bullets
        self.role = role
        self.character = character
        self.gunCard = Card('Colt.45', 'EG', None, None, 100)
        self.equipmentCards = None


