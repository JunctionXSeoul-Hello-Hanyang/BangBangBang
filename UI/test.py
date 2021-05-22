from DrawUi import DrawUi
from BoardSection import BoardSection,BoardEntity
import os
import time

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

ui.draw_total()

time.sleep(5000)