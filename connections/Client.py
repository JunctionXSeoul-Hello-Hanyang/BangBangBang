import pygame
from Network import Network
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Rule import Board



width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
clientNumber = 0

turn_over_button = None # turn over 해주는 button
cards = None # 현재 가지고 있는 카드
card_use_button = None

def showCardOnRight(board, idx):
    return 0

# use card right
# 예외 처리 중요 ex) 총 장착 여러개 안됨, bang 여러개 사용 못함
def useCardOnRight(board, idx):
    return 0

def discard_card(board, idx):
    return 0

if __name__ == "__main__":
    run = True

    network = Network("18.191.254.252", 5555)
    my_player_number = network.id
    clock = pygame.time.Clock()
    phase = '0'

    while run:
        clock.tick(60)
        board = network.send('update')

        for event in pygame.event.get():
            if board.whosturn == my_player_number:
                # phase2 (use card)
                if board.phase == '2':
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        # turn over button
                        if turn_over_button.collidepoint(event.pos):
                            board.phase = '3'
                        # select card
                        for idx, card in enumerate(cards):
                            if card.collidepoint(event.pos):
                                showCardOnRight(board, idx)
                        if card_use_button.collidepoint(event.pos):
                            useCardOnRight(board, idx)
                # phase 3 (exceed card)
                elif phase == '3':
                    if len(board.players[my_player_number].cards) > board.players[my_player_number].field.bullets:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            for idx, card in enumerate(cards):
                                if card.collidepoint(event.pos):
                                    discard_card(board,idx)
                    else:
                        phase = '4'
                # phase 4 (turn over)
                elif phase == '4':
                    board = network.send('turn over')

            elif event.type == pygame.QUIT:
                run = False
                pygame.quit()
                network.close()
                print('Quit')



