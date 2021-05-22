from pygame.locals import *
import pygame
import os
import time
from UI import BoardSection

class DrawUi:
    def __init__(self,X=1280,Y=720,):
        self.cards_path = "../UI/ImageAsset/cards/"
        self.screen = pygame.display.set_mode((X,Y), DOUBLEBUF)
        pygame.display.set_caption('Bang Board')
        self.BoardBaseImage = pygame.image.load("../UI/ImageAsset/BoardBase.png").convert_alpha()
        self.rects = { i:None for i in range(40)}
        self.board = BoardSection.BoardSection()
        
        
    def update_card(self,index,card):
        self.board.boardSection[index].card = card

    def draw_one(self,card, box, index, condition = -1):
        if index == 38:
            image = pygame.image.load(self.cards_path + "use" + '.png')
        elif index == 39:
            image = pygame.image.load(self.cards_path + "turn_over" + '.png')
        else:
            if card == 0:
                return 0
            image = pygame.image.load(self.cards_path + card.name + '.png')

                                    
           
        image = pygame.transform.scale(image, (box.width, box.height))
        rect = image.get_rect()
        rect.center = (box.centerX,box.centerY)
        self.rects[index] = rect
        self.screen.blit(image, rect)
    
    def draw_total(self):
        self.screen.fill((255,255,255))
        self.screen.blit(self.BoardBaseImage, (0, 0))
        
        for idx, current in enumerate(self.board.boardSection):
            self.draw_one(current.card,current.boardLocation, idx)
        pygame.display.update()
