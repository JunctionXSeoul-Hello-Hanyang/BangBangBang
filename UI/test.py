from DrawUi import DrawUi
from BoardSection import BoardSection,BoardEntity
import os
import sys
import time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Card import Card
from Rule.Player import Player

class Card:
    def __init__(self, name, type, number, trump_symbol, idx):
        self.name = name
        self.number = number
        self.trump_symbol = trump_symbol
        self.type = type
        self.idx = idx

p1 = Player(0, 2,"outlaw" , "", [Card("back-playing",0,0,0,0),Card("bang",0,0,0,0),Card("barrel",0,0,0,0)])

ui = DrawUi(0,[1,2,3,4])

path = "./ImageAsset/cards/"
file_list = os.listdir(path) + os.listdir(path) + os.listdir(path)

class Card:
    def __init__(self, name, type, number, trump_symbol, idx):
        self.name = name
        self.number = number
        self.trump_symbol = trump_symbol
        self.type = type
        self.idx = idx
    


for i in range(20):
    ui.update_card(i,Card(file_list[i].replace(".png",""),0,0,0,0))
ui.update_player(p1)
ui.draw_total()

time.sleep(5000)