from Rule import *
from Card import *
import random

class Board:
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.number_of_playingCards = 80

        self.players = None
        self.deck = None
        self.trashCan = None

    def gameStart(self):
        role_temp = random.shuffle(Setting.NUMBER_OF_ROLE[self.number_of_players])
        self.players = [Player() for i in range(self.number_of_players)]
        self.deck = initDeck()


    def initDeck(self):









