from DrawUi import DrawUi
from BoardSection import BoardSection,BoardEntity
import os
import time

ui = DrawUi()
b_list   = BoardSection().boardSection

print(b_list)

path = "./ImageAsset/cards/"
file_list = os.listdir(path) + os.listdir(path) + os.listdir(path)

class Card:
    def __init__(self, name, type, number, trump_symbol, idx):
        self.name = name
        self.number = number
        self.trump_symbol = trump_symbol
        self.type = type
        self.idx = idx
    




input_list = [[Card(file_list[i].replace(".png",""),0,0,0,0),b_list[i].boardLocation] for i in range(40)]

ui.update(input_list)

time.sleep(5000)