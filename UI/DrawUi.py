from pygame.locals import *
import pygame
import os,sys
import time
from UI import BoardSection
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Card import Card

from tkinter import *
from tkinter import messagebox

class DrawUi:

    def __init__(self,current_player,other_player_list,X=1280,Y=720):
        
        self.current_player = current_player
        self.other_player_list = other_player_list
        
        self.cards_path = "../UI/ImageAsset/cards/"
        self.screen = pygame.display.set_mode((X,Y), DOUBLEBUF)
        pygame.display.set_caption('Bang Board')
        self.BoardBaseImage = pygame.image.load("../UI/ImageAsset/BoardBase.png").convert_alpha()
        
        self.board = BoardSection.BoardSection([current_player] + other_player_list)
        
        self.rects = {i:None for i in range(40)}
        
        
    def update_card(self,index,card):
        self.board.boardSection[index].card = card

        
    def update_player(self,player):
        index = self.board.player_dict[player.player_number]
        if index == 0:
            
            self.update_card(self.board.UI_dict[index][0],Card(player.field.role,0,0,0,0)) # not yet
            self.update_card(self.board.UI_dict[index][1],player.field.equipmentCards)
            self.update_card(self.board.UI_dict[index][2],player.field.gunCard)
            self.update_card(self.board.UI_dict[index][3],Card(str(player.field.bullets),0,0,0,0))
            
            for i,card in enumerate(player.cards):
                self.update_card(self.board.UI_dict[index][4+i],card)
                
                
        else:
            self.update_card(self.board.UI_dict[index][0],Card(str(player.player_number),0,0,0,0))
            self.update_card(self.board.UI_dict[index][1],Card(player.field.role,0,0,0,0))
            self.update_card(self.board.UI_dict[index][2],player.field.equipmentCards)
            self.update_card(self.board.UI_dict[index][3],Card(str(len(player.cards)),0,0,0,0))
            self.update_card(self.board.UI_dict[index][4],player.field.gunCard)
            self.update_card(self.board.UI_dict[index][5],Card(str(player.field.bullets),0,0,0,0))
            
        
    def draw_one(self,card,box,condition = -1):

        if condition == -1:
            image = pygame.image.load(self.cards_path + card.name + '.png')                
         
        image = pygame.transform.scale(image, (box.width, box.height))
        rect = image.get_rect()
        rect.center = (box.centerX,box.centerY)
        self.rects[box.sectionNumber] = rect
                
        self.screen.blit(image, rect)
    
    def draw_total(self):
        self.screen.fill((255,255,255))
        self.screen.blit(self.BoardBaseImage, (0, 0))
        for current in self.board.boardSection:
            condition = -1
            
            if current.boardLocation.sectionNumber == 38:
                current.card = Card("use",0,0,0,0)
            elif current.boardLocation.sectionNumber == 39:
                current.card = Card("turn_over",0,0,0,0)
                
            elif current.card == 0 or current.card == None:
                current.card = Card("X",0,0,0,0)
            
            self.draw_one(current.card,current.boardLocation,condition)
        pygame.display.update()

    def popUp(self, message="a"):
        Tk().wm_withdraw() #to hide the main window
        messagebox.showinfo('Continue',message)