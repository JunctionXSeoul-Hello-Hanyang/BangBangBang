import pygame
from Network import Network
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Rule import Board
from Rule import Setting



width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
clientNumber = 0

turn_over_button = None # turn over 해주는 button
cards = None # 현재 가지고 있는 카드
players = None # 상대 playser
card_use_button = None # 오른쪽 card의 use button
right_card_idx = -1 # 오른쪽에 card의 deck_idx

def available_player(board, right_card_idx, my_player_number, target_player_number):
    # bang일때 장착한 권총 사정거리를 벗어나면 False return
    distance = min(abs(my_player_number - target_player_number), abs(target_player_number - my_player_number))
    if Setting.PLAYING_CARD[right_card_idx][0] == 'bang':
        if distance > Setting.GUN_RANGE[board.players[my_player_number].field.gunCard.name]:
            return False
    elif Setting.PLAYING_CARD[right_card_idx][0] == 'panic':
        if distance > 1:
            return False
    return True

def select_target_player(board, right_card_idx, my_player_number):
    player_idx = -1
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, player in enumerate(players):
                if player.collidepoint(event.pos) and available_player(board, right_card_idx, my_player_number, i):
                    player_idx = i
    return player_idx

def showCardOnRight(board, idx):
    return 0

# use card right
# 예외 처리 중요 ex) 총 장착 여러개 안됨, bang 여러개 사용 못함
def useCardOnRight(board, idx):

    return 0 # target이 필요하면 1 안필요하면 0

def discard_card(board, idx):
    return 0

board = Board.Board(5)
if __name__ == "__main__":
    run = True

    network = Network("18.191.254.252", 5555)
    my_player_number = network.id
    clock = pygame.time.Clock()
    phase = '0'

    while run:
        clock.tick(60)
        #board = network.send('update')

        for event in pygame.event.get():
            if board.whoseTurn == my_player_number:

                # phase2 (use card)
                if board.phase == '2':
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        # turn over button
                        if turn_over_button.collidepoint(event.pos):
                            board.phase = '3'
                        # select card
                        for i, card in enumerate(cards):
                            if card.collidepoint(event.pos):
                                right_card_idx = showCardOnRight(board, i)
                        if card_use_button.collidepoint(event.pos):
                            target_player_idx = -1
                            hasTarget = useCardOnRight(board, right_card_idx)
                            if hasTarget == True:
                                target_player_idx = select_target_player(board, right_card_idx, my_player_number)
                            board = network.send('bang {} {} {}'.format(my_player_number, target_player_idx, right_card_idx))

                # phase 3 (exceed card)
                elif board.phase == '3':
                    if len(board.players[my_player_number].cards) > board.players[my_player_number].field.bullets:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            for idx, card in enumerate(cards):
                                if card.collidepoint(event.pos):
                                    discard_card(board,idx)
                    else:
                        board.phase = '4'
                # phase 4 (turn over)
                elif board.phase == '4':
                    board = network.send('turn over')

            elif event.type == pygame.QUIT:
                run = False
                pygame.quit()
                network.close()
                print('Quit')



