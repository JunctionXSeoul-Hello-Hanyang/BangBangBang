import pygame
import random
from Network import Network
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Rule import Board
from Rule import Setting

from UI import DrawUi
from Card import Card
import time

'''
width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
'''
clientNumber = 0
my_player_number = 0

cnt = {'gun': 0, 'bang': 0}

drawUI = None
other_player = [i for i in range(5)] # 나를 제외한 player의 number
turn_over_button = None # turn over 해주는 button
cards = [] # 현재 가지고 있는 카드
players = [] # 상대 플레이어들
card_use_button = None # 오른쪽 card의 use button
right_card_idx = -1 # 오른쪽에 card의 deck_idx


def victoryConditions(board):
    dieRole = []
    for player in board.players:
        if player.field.bullets <= 0:
            dieRole.append(player.field.role)
    # 배신자 승리
    if dieRole.count('renegade') == 0 and len(dieRole) == 4:
        return 'renegade'
    #무법자 승릐
    elif dieRole.count('sheriff') == 1:
        return 'outlaw'
    #보안관 부곤 승리
    elif dieRole.count('renegade') == 1 and dieRole.count('outlaw') == 2:
        return 'sheriff and deputy'
    else:
        return None

def available_player(board, right_card_idx, my_player_number, target_player_number):
    # bang일때 장착한 권총 사정거리를 벗어나면 False return
    distance = min(abs(my_player_number - target_player_number), abs(5-abs(target_player_number - my_player_number)))
    if Setting.PLAYING_CARD[right_card_idx][0] == 'bang':
        if distance > Setting.GUN_RANGE[board.players[my_player_number].field.gunCard.name]:
            drawUI.popUp('The enemy is out of range.')
            return False
    elif Setting.PLAYING_CARD[right_card_idx][0] == 'panic':
        if distance > 1:
            drawUI.popUp('The enemy is out of range.')
            return False
    elif Setting.PLAYING_CARD[right_card_idx][0] == 'catBalu':
        if len(board.players[target_player_number].cards) == 0:
            drawUI.popUp('He has 0 cards')
            return False
    return True

def select_target_player(board, card_idx, my_player_number):
    player_idx = -1
    while player_idx == -1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, player in enumerate(players):
                    if player.collidepoint(event.pos) and available_player(board, card_idx, my_player_number, other_player[i]):
                        player_idx = other_player[i]
    return player_idx

def select_target_card(board, card_idx, my_player_number):
    # 장착된 카드 선택 혹은 랜덤하게 상대 패 선택
    player_idx = -1
    while player_idx == -1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, player in enumerate(players):
                    if player.collidepoint(event.pos) and available_player(board, card_idx, my_player_number, i):
                        player_idx = other_player[i]
                        print(player_idx)
    pick_card = random.choice(board.players[player_idx].cards)
    print('pick_card: ', pick_card.idx)
    return pick_card.idx

def showCardOnRight(board, idx, cards):
    print('showCardOnRight')
    card = board.players[my_player_number].cards[idx]

    drawUI.update_card(37, card)
    display_update(board, cards)

    return card.idx

# use card right
# 예외 처리 중요 ex) 총 장착 여러개 안됨, bang 여러개 사용 못함
def useCardOnRight(board, idx):
    result = -1
    card = Setting.PLAYING_CARD[idx]
    if card[0] == 'bang':
        if cnt['bang'] <1:
            target_player_idx = select_target_player(board, idx, my_player_number)
            result = 'bang {} {}'.format(idx, target_player_idx)
            cnt['bang'] +=1
        else:
            drawUI.popUp('You already used a bang card this turn.')
    elif card[0] == 'missed':
        result = -1
    elif card[0] == 'beer':
        result = 'beer {}'.format(idx)
    elif card[0] == 'duel':
        target_player_idx = select_target_player(board, idx, my_player_number)
        result = 'duel {} {}'.format(idx, target_player_idx)
    elif card[0] == 'indian':
        result = 'indian {}'.format(idx)
    elif card[0] == 'gatling':
        result = 'gatling {}'.format(idx)
    elif card[0] == 'saloon':
        result = 'saloon {}'.format(idx)
    elif card[0] == 'panic':
        target_card_idx = select_target_card(board, idx, my_player_number)
        result = 'panic {} {}'.format(idx, target_card_idx)
    elif card[0] == 'catBalu':
        target_card_idx = select_target_card(board, idx, my_player_number)
        result = 'catBalu {} {}'.format(idx, target_card_idx)
    elif card[0] == 'generalStore':
        result = 'generalStore {}'.format(idx)
    elif card[0] == 'stagecoach':
        result = 'stagecoach {}'.format(idx)
    elif card[0] == 'wellsFargo':
        result = 'wellsFargo {}'.format(idx)

    return result

def display_update(board, cards, turn_change = 0):
    cards.clear()
    players.clear()

    win_role = victoryConditions(board)
    if win_role != None:
        if win_role == board.players[my_player_number].feild.role:
            drawUI.popUp('WIN!!!')
        else:
            drawUI.popUp('LOSE...')

    # 턴이 바뀐 시점에 rightImage 자리에 'yourTurn.png'를 켜준다.
    if turn_change == 1:
        drawUI.update_card(37, Card('yourTurn', 0, 0, 0, 0))

    # 상대방의 상태 update(Player 객체를 통해)
    drawUI.update_player(board.players[my_player_number])
    for other_person in other_player:
        drawUI.update_player(board.players[other_person])

    # 자신의 패 update
    for i, card in enumerate(board.players[my_player_number].cards):
        idx = 28 + i
        drawUI.update_card(idx, card)
    drawUI.draw_total()



    # cards update
    for i, card in enumerate(board.players[my_player_number].cards):
        idx = 28 + i
        cards.append(drawUI.rects[idx])

    # players update (player의 bullets)
    for i, player_idx in enumerate(other_player):
        idx = 6 * (i+1) -1
        players.append(drawUI.rects[idx])



#board = Board.Board(5)
#board.phase = '2'

board = 0
turn = 0
if __name__ == "__main__":
    run = True
    network = Network("18.191.254.252", 5556)
    #network = Network("127.0.0.1", 5555)
    my_player_number = int(network.id)
    del other_player[my_player_number]
    clock = pygame.time.Clock()

    board = network.send('update')
    drawUI = DrawUi.DrawUi(my_player_number, other_player)
    display_update(board, cards)
    phase = board.phase
    card_use_button = drawUI.rects[38]
    turn_over_button = drawUI.rects[39]


    while run:
        clock.tick(60)
        if board.whoseTurn != my_player_number :
            turn = 0
            prev = board.whoseTurn
            board = network.send('update')
            if board.whoseTurn != prev:
                display_update(board, cards)

        for event in pygame.event.get():
            if board.whoseTurn == my_player_number:
                if turn == 0:
                    display_update(board, cards, 1)
                turn = 1

                # phase2 (use card)
                if phase == '2':
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        # turn over button
                        if turn_over_button.collidepoint(event.pos):
                            phase = '3'
                        # card use button
                        elif card_use_button.collidepoint(event.pos):
                            print('click')
                            msg = useCardOnRight(board, right_card_idx)
                            if msg != -1: # 사용할수 있는 카드인 경우
                                board = network.send(msg)
                                display_update(board, cards)

                        # select card
                        for i, card in enumerate(cards):
                            if card.collidepoint(event.pos):
                                right_card_idx = showCardOnRight(board, i, cards)

                # phase 3 (exceed card)
                elif phase == '3':
                    if len(board.players[my_player_number].cards) > board.players[my_player_number].field.bullets:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            for idx, card in enumerate(cards):
                                if card.collidepoint(event.pos):
                                    card_idx = board.players[my_player_number].cards[idx].idx
                                    board = network.send('discard {}'.format(card_idx))
                                    display_update(board, cards)

                    else:
                        board = network.send('turn over')  # turn over
                        cnt['bang'] = 0
                        cnt['gun'] = 0
                        display_update(board, cards)
                        phase = board.phase

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                network.close()
                print('Quit')




