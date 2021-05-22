from pygame.locals import *
import pygame
import os
import time
from BoardSection import BoardSection
class DrawUi:
    def __init__(self,X=1280,Y=720,):
        self.cards_path = "./ImageAsset/cards/"
        self.screen = pygame.display.set_mode((X,Y), DOUBLEBUF)
        pygame.display.set_caption('Bang Board')
        self.BoardBaseImage = pygame.image.load("./ImageAsset/BoardBase.png").convert_alpha()
        
        self.board = BoardSection()
        
        
    def update_card(self,index,card):
        self.board.boardSection[index].card = card
        
    def draw_one(self,card,box,condition = -1):
        if condition == -1:
            image = pygame.image.load(self.cards_path + card.name + '.png')
            
        if condition == 38:
            image = pygame.image.load(self.cards_path + "use" + '.png')
        
        elif condition == 39:
            image = pygame.image.load(self.cards_path + "turn_over" + '.png')
                                      
                                    
           
        image = pygame.transform.scale(image, (box.width, box.height))
        rect = image.get_rect()
        rect.center = (box.centerX,box.centerY)
        self.screen.blit(image, rect)
    
    def draw_total(self):
        self.screen.fill((255,255,255))
        self.screen.blit(self.BoardBaseImage, (0, 0))
        
        for current in self.board.boardSection:
            self.draw_one(current.card,current.boardLocation)
        pygame.display.update()
