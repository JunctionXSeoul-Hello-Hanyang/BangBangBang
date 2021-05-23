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

p0 = Player(0, 2,"outlaw" , "", [Card("back-playing",0,0,0,0),Card("bang",0,0,0,0),Card("barrel",0,0,0,0)])
p1 = Player(1, 2,"deputy" , "", [Card("back-playing",0,0,0,0),Card("bang",0,0,0,0),Card("barrel",0,0,0,0)])
p2 = Player(2, 2,"renegade" , "", [Card("back-playing",0,0,0,0),Card("bang",0,0,0,0),Card("barrel",0,0,0,0)])
p3 = Player(3, 2,"sheriff" , "", [Card("back-playing",0,0,0,0),Card("bang",0,0,0,0),Card("barrel",0,0,0,0)])
p4 = Player(4, 2,"vice" , "", [Card("back-playing",0,0,0,0),Card("bang",0,0,0,0),Card("barrel",0,0,0,0)])




ui = DrawUi(3,[1,2,0,4])

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
ui.update_player(p0)
ui.update_player(p1)
ui.update_player(p2)
ui.update_player(p3)
ui.update_player(p4)

ui.highlight(5)
ui.draw_total()

time.sleep(5000)