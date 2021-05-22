from Rule import Setting
from Rule import Player
from Card import Card
import random

class Board:
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.number_of_playingCards = 80

        self.deck = []
        self.players = []
        self.trashCan = []

        self.whoseTurn = 0
        self.phase = '2'


        # shuffle deck
        for idx, card in enumerate(Setting.PLAYING_CARD):
            self.deck.append(Card(card[0], card[1], card[2], card[3], idx))
        random.shuffle(self.deck)

        # init player, draw cards
        random.shuffle(Setting.NUMBER_OF_ROLE[self.number_of_players])
        for player_number in range(self.number_of_players):
            init_role = Setting.NUMBER_OF_ROLE[self.number_of_players][player_number]
            init_bullets = 4 + (init_role == 'Sheriff')  # 보안관은 bullets + 1

            self.players.append(Player.Player(player_number, init_bullets, init_role, None, self.deck[-init_bullets:]))
            del self.deck[-init_bullets:]


















