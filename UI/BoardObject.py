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

        self.baseLocation = np.array([41,33]) + np.array([playerOrder*196, 0])
        
        self.nameLocation = self.baseLocation + (self.width / 2)
        self.roleLocation = self.baseLocation + (self.width / 4) + (self.height / 4)
        self.equipmentLocation = self.baseLocation + (self.width / 4 * 3) + (self.height / 4)
        self.gunLocation = self.baseLocation + (self.width / 4) + (self.height / 4 * 3)
        self.numOfCardsLocation = self.baseLocation + (self.width / 4 * 3) + (self.height / 4 * 3)
        self.healthLocation = self.baseLocation + (self.width / 2) + (self.height)

        self.nameImage = pygame.image.load(self.ROLE_PATH + "ROLE_UNKNOWN" + '.png')
        self.roleImage = pygame.image.load(self.ROLE_PATH + "ROLE_UNKNOWN" + '.png')
        self.equipmentImage = pygame.image.load(self.ROLE_PATH + "ROLE_UNKNOWN" + '.png')
        self.gunImage = pygame.image.load(self.ROLE_PATH + "ROLE_UNKNOWN" + '.png')
        self.numOfCardsImage = pygame.image.load(self.ROLE_PATH + "ROLE_UNKNOWN" + '.png')
        self.healthImage = pygame.image.load(self.ROLE_PATH + "ROLE_UNKNOWN" + '.png')

    def updateImage(self):
        # health, Role 등 정해진 변수에 따른 이미지 가져오기
        # 아래는 health와 같이 숫자를 출력하기 위한 폰트 가져오기
        font = pygame.font.SysFont(None, 100)
        
        self.roleImage = pygame.image.load(self.ROLE_PATH + self.role + '.png').convert()
        # 이미지 리사이징
        self.roleImage = pygame.transform.scale(self.roleImage, (80, 120))
        # 이미지 좌표 가운데로 정렬
        self.role_rect = self.roleImage.get_rect()
        self.role_rect.center = self.roleLocation
        

        # 장비 이미지 업로드
        if self.equipment is 'NO_EQUIPMENT':            
            # 장비가 없을 때는 X라고 표시하기 위해 글자를 넣는다.
            self.equipmentImage = font.render('X', True, (100, 100, 100))
        else:
            self.equipmentImage = pygame.image.load(self.EQUIPMENT_PATH + self.equipment + '.png')
            self.equipmentImage = pygame.transform.scale(self.equipmentImage, (80, 120))

        self.equipment_rect = self.equipmentImage.get_rect()
        self.equipment_rect.center = self.equipmentLocation

        # 총 이미지 업로드
        if self.gun is 'NO_GUN':            
            self.gunImage = font.render('X', True, (100, 100, 100))
        else:
            self.gunImage = pygame.image.load(self.GUN_PATH + self.gun + '.png')
            self.gunImage = pygame.transform.scale(self.gunImage, (80, 120))

        self.gun_rect = self.gunImage.get_rect()
        self.gun_rect.center = self.gunLocation

        # 카드 개수 이미지 업로드
        self.numOfCardsImage = font.render(str(self.numOfCards), True, (100, 100, 100))
        self.numOfCards_rect = self.numOfCardsImage.get_rect()
        self.numOfCards_rect.center = self.numOfCardsLocation
   
        # 체력 이미지 업로드
        self.healthImage = font.render(str(self.health), True, (255, 0, 0))
        self.health_rect = self.healthImage.get_rect()
        self.health_rect.center = self.healthLocation


        # 플레이어 이름 업로드
        font = pygame.font.SysFont(None, 50)
        self.nameImage = font.render(str(self.name), True, (100, 100, 100))
        self.name_rect = self.nameImage.get_rect()
        self.name_rect.center = self.nameLocation