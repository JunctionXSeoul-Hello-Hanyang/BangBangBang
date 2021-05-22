import pygame
import numpy as np
from pygame.locals import *

class EnemyStatus:
    def __init__(self, name, playerOrder, health, numOfCards, role, gun, equipment):
        self.ROLE_PATH = './ImageAsset/Roles/'
        self.EQUIPMENT_PATH = './ImageAsset/Equipment/'
        self.GUN_PATH = './ImageAsset/Gun/'

        self.name = name
        self.playerOrder = playerOrder
        self.health = health
        self.numOfCards = numOfCards
        self.role = role
        self.gun = gun
        self.equipment = equipment

        # 각 이미지의 좌표 정하기
        self.width = np.array([196, 0])
        self.height = np.array([0, 303])

        self.baseLocation = np.array([51,43]) + np.array([playerOrder*196, 0])
        
        self.roleLocation = self.baseLocation
        self.equipmentLocation = self.baseLocation + self.width / 2
        self.gunLocation = self.baseLocation + self.height / 2
        self.numOfCardsLocation = self.baseLocation + (self.width + self.height) / 2
        self.healthLocation = self.baseLocation + (self.width / 2) + self.height

    def updateImage(self):
        # health, Role 등 정해진 변수에 따른 이미지 가져오기
        # 아래는 health와 같이 숫자를 출력하기 위한 폰트 가져오기
        font = pygame.font.SysFont(None, 100)
        
        self.roleImage = pygame.image.load(self.ROLE_PATH + self.role + '.png')
        # 이미지 리사이징
        self.roleImage = pygame.transform.scale(self.roleImage, (80, 120))

        if self.equipment is 'NO_EQUIPMENT':            
            # 장비가 없을 때는 X라고 표시하기 위해 글자를 넣는다.
            self.equipmentImage = font.render('X', True, (100, 100, 100))
        else:
            self.equipmentImage = pygame.image.load(self.EQUIPMENT_PATH + self.equipment + '.png')

        if self.gun is 'NO_GUN':            
            self.gunImage = font.render('X', True, (100, 100, 100))
        else:
            self.gunImage = pygame.image.load(self.EQUIPMENT_PATH + self.equipment + '.png')

        self.numOfCardsImage = font.render(str(self.numOfCards), True, (100, 100, 100))
        self.healthImage = font.render(str(self.health), True, (100, 100, 100))



        #self.numOfCardsImage = self.equipmentImage = pygame.image.load(self.ROLE_PATH + self.role + '.png')

        ## health
