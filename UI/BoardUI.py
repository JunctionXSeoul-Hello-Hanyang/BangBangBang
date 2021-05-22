import pygame
from pygame.locals import *

class BoardUI:
    def __init__(self, BoardX=1782, BoardY=720):
        # pyGame 라이브러리 초기화
        pygame.init()

        # 디스플레이 초기화
        self.BoardX = BoardX
        self.BoardY = BoardY
        self.screen = pygame.display.set_mode((self.BoardX, self.BoardY), DOUBLEBUF)
        # 타이틀바 텍스트 설정
        pygame.display.set_caption('Bang Board')

        # 기본 보드 그리기
        print("print board")
        self.drawBoard()

    def drawBoard(self):
        BoardBase = pygame.image.load("./ImageAsset/BoardBase.png").convert_alpha()
        self.screen.blit(BoardBase, (0, 0))
        pygame.display.update() 
        return 0
    
    def drawCard(self, cardType, location):
        # draw 'cardType' at 'location'
        return 0
