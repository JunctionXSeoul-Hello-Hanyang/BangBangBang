from pygame.locals import *
import pygame
import os
import time
class DrawUi:
    def __init__(self,X=1280,Y=720,):
        self.cards_path = "./ImageAsset/cards/"
        self.screen = pygame.display.set_mode((X,Y), DOUBLEBUF)
        pygame.display.set_caption('Bang Board')
        self.BoardBaseImage = pygame.image.load("./ImageAsset/BoardBase.png").convert_alpha()
        
    def draw_one(self,card,box):
        print(self.cards_path + card.name + '.png')
        image = pygame.image.load(self.cards_path + card.name + '.png')
        image = pygame.transform.scale(image, (box.width, box.height))
        rect = image.get_rect()
        rect.center = (box.centerX,box.centerY)
        self.screen.blit(image, rect)
        
    def update(self,update_list):
        self.screen.fill((255,255,255))
        self.screen.blit(self.BoardBaseImage, (0, 0))
        for current in update_list:
            self.draw_one(current[0],current[1])
        pygame.display.update()
