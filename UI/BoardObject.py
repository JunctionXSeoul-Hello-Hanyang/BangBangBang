import pygame
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

        self.width = {196, 0}
        self.height = {0, 303}
        self.baseLocation = {41,33} + {playerOrder*196, 0}
        
        self.roleLocation = self.baseLocation
        self.equipmentLocation = self.baseLocation + self.width / 2
        self.gunLocation = self.baseLocation + self.height / 2
        self.numOfCardsLocation = self.baseLocation + (self.width + self.health) / 2

    def updateImage(self):
        font = pygame.font.Font('LexiGulim.ttf', 30)
        
        self.roleImage = pygame.image.load(self.ROLE_PATH + self.role + '.png')

        if self.equipment is 'NO_EQUIPMENT':            
            self.equipmentImage = font.render('X', True(28,0,0))
        else:
            self.equipmentImage = pygame.image.load(self.EQUIPMENT_PATH + self.equipment + '.png')

        if self.gun is 'NO_GUN':            
            self.gunImage = font.render('X', True(28,0,0))
        else:
            self.gunImage = pygame.image.load(self.EQUIPMENT_PATH + self.equipment + '.png')

        self.numOfCardsImage = font.render(self.numOfCards, True(28, 0, 0))

        ## health