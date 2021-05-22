from DrawUi import DrawUi
from BoardSection import BoardSection,BoardEntity
import os
import time
import pygame

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

print()

ui.draw_total()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            a = ui.getClickInfo(event.pos)

            if a == 0:
                continue
            if a.card.name == "mustang":
                print("MUSTANG!")

        elif event.type == pygame.QUIT:
            pygame.quit()
            print('Quit')

