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


        # shuffle deck
        random.shuffle(Setting.PLAYING_CARD)
        for card in Setting.PLAYING_CARD:
            self.deck.append(Card(card[0], card[1], card[2], card[3]))

        # init player, draw cards
        random.shuffle(Setting.NUMBER_OF_ROLE[self.number_of_players])
        for player_number in range(self.number_of_players):
            init_role = Setting.NUMBER_OF_ROLE[self.number_of_players][player_number]
            init_bullets = 4 + (init_role == 'Sheriff')  # 보안관은 bullets + 1

            self.players.append(Player.Player(player_number, init_bullets, init_role, None, self.deck[-init_bullets:]))
            del self.deck[-init_bullets:]


    # 현재 순서의 플레이어가 카드 한 장 뽑는 함수
    def drawCard(self):
        # deck에서 카드 한 개 뽑음
        drawedCard = self.deck.pop();

        # 현재 차례의 플레이어를 선택해 해당 플레이어의 덱에 추가해준다.
        curPlayer = self.players[self.whoseTurn]
        curPlayer.cards.append(drawedCard);

        # deck 비어있는 경우, 버려진 덱을 섞어서 채워준다.
        if self.deck:
            random.shuffle(self.trashCan)
            self.deck = self.trashCan
            self.trashCan = []















