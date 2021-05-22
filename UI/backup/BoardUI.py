import pygame
from pygame.locals import *
from BoardObject import EnemyStatus

class BoardUI:
    def __init__(self, myName, playerName, BoardX=1280, BoardY=720):
        pygame.init()

        self.myName = myName
        self.enemyStatusList = []
        i = 0
        for temp in playerName:
            self.enemyStatusList.append(EnemyStatus(temp, i, 0, 0, 0, 0, 0))
            i += 1

        self.BoardX = BoardX
        self.BoardY = BoardY
        self.screen = pygame.display.set_mode((self.BoardX, self.BoardY), DOUBLEBUF)
        # 타이틀바 텍스트 설정
        pygame.display.set_caption('Bang Board')

        # 기본 보드 가져오기
        self.BoardBaseImage = pygame.image.load("./ImageAsset/BoardBase.png").convert_alpha()

    def drawBoard(self):
        # 초기화
        print("초기화")
        self.screen.fill((255,255,255))

        # 보드 그리기
        print("print board")
        self.screen.blit(self.BoardBaseImage, (0, 0))

        # 적 상태 그리기
        # BoardObject의 EnemyStatus Class에 저장된 이미지를 그려준다.
        print("print enemystatus")
        for temp in self.enemyStatusList:
            self.screen.blit(temp.nameImage, temp.name_rect)
            self.screen.blit(temp.roleImage, temp.role_rect)
            self.screen.blit(temp.equipmentImage, temp.equipment_rect)
            self.screen.blit(temp.gunImage, temp.gun_rect)
            self.screen.blit(temp.numOfCardsImage, temp.numOfCards_rect)
            self.screen.blit(temp.healthImage, temp.health_rect)
            

        pygame.display.update() 

    # Client가 UI에 접근하기 위한 함수
    def drawEnemyStatus(self, playerName, health, numOfCards, role="ROLE_UNKNOWN", gun="NO_GUN", equipment="NO_EQUIPMENT"):
        i = "ERROR"
        
        for temp in self.enemyStatusList:
            if temp.name != playerName:
                continue
            
            i = "NOT ERROR"
            temp.health = health
            temp.numOfCards = numOfCards
            temp.role = role
            temp.gun = gun
            temp.equipment = equipment

            temp.updateImage()

        if i is "ERROR":
            print("no player name match")
            print("error occured at drawEnemyStatus")
            return -1

        return 0


    def drawInteractionSection(self, cardName, useButton="NO_BUTTON"):
        pass