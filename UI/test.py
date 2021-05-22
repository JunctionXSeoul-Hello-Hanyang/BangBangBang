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
        image = pygame.image.load(self.cards_path + card.name + '.png')
        image = pygame.transform.scale(image, (box[0], box[1]))
        rect = image.get_rect()
        rect.center = (box[2],box[3])
        self.screen.blit(image, rect)
    def update(self,update_list):
        self.screen.fill((255,255,255))
        self.screen.blit(self.BoardBaseImage, (0, 0))
        for current in update_list:
            self.draw_one(current[0],current[1])
        pygame.display.update()
class Card:
    def __init__(self, name, type, number, trump_symbol, idx):
        self.name = name
        self.number = number
        self.trump_symbol = trump_symbol
        self.type = type
        self.idx = idx
card1 = Card("appaloosa",0,0,0,0)
box1 = [100,100,50,50]
com_list = [[card1,box1]]
card2 = Card("indians",0,0,0,0)
box2 = [350,350,300,300]
com_list = [[card2,box2],[card1,box1]]
ui = DrawUi()
ui.update(com_list)
time.sleep(5000)