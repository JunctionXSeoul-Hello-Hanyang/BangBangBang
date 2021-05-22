from pygame.locals import *
import pygame
import os,sys
import time
from BoardSection import BoardSection

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Card import Card



class DrawUi:
    def __init__(self,current_player,X=1280,Y=720):
        
        self.current_player = current_player
        
        self.cards_path = "./ImageAsset/cards/"
        self.screen = pygame.display.set_mode((X,Y), DOUBLEBUF)
        pygame.display.set_caption('Bang Board')
        self.BoardBaseImage = pygame.image.load("./ImageAsset/BoardBase.png").convert_alpha()
        
        self.board = BoardSection()
        
        
    def update_card(self,index,card):
        self.board.boardSection[index].card = card
        
    def update_player(self,player):
        return
        
    def draw_one(self,card,box,condition = -1):
        if condition == -1:
            image = pygame.image.load(self.cards_path + card.name + '.png')                
           
        image = pygame.transform.scale(image, (box.width, box.height))
        rect = image.get_rect()
        rect.center = (box.centerX,box.centerY)
        self.screen.blit(image, rect)
        return
    
    def draw_total(self):
        self.screen.fill((255,255,255))
        self.screen.blit(self.BoardBaseImage, (0, 0))
        for current in self.board.boardSection:
            condition = -1
            
            if current.boardLocation.sectionNumber == 38:
                current.card = Card("use",0,0,0,0)
            elif current.boardLocation.sectionNumber == 39:
                current.card = Card("turnover",0,0,0,0)
                
            elif current.card == 0:
                current.card = Card("X",0,0,0,0)
            
            self.draw_one(current.card,current.boardLocation,condition)
        pygame.display.update()
