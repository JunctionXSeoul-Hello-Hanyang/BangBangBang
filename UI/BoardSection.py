import numpy as np

# width, height, center
BOARD_LIST = [
############################# Top Left First Section
[80, 120, 136, 30],         # 0
[80, 120, 88, 108],         # 1
[80, 120, 184, 108],        # 2
[80, 120, 88, 259],         # 3
[80, 120, 184, 259],        # 4
[80, 120, 136, 338],        # 5

############################# Top Left Second Section
[80, 120, 332, 30],         # 6
[80, 120, 284, 108],        # 7
[80, 120, 380, 108],        # 8
[80, 120, 284, 259],        # 9
[80, 120, 380, 259],        # 10
[80, 120, 332, 338],        # 11

############################# Top Left Third Section
[80, 120, 528, 30],         # 12
[80, 120, 480, 108],        # 13
[80, 120, 576, 108],        # 14
[80, 120, 480, 259],        # 15
[80, 120, 576, 259],        # 16
[80, 120, 528, 338],        # 17

############################# Top Left Fourth Section
[80, 120, 725, 30],         # 18
[80, 120, 677, 108],        # 19
[80, 120, 773, 108],        # 20
[80, 120, 677, 259],        # 21
[80, 120, 773, 259],        # 22
[80, 120, 725, 338],        # 23

############################# My Status Section
[80, 120, 136, 432],        # 24
[80, 120, 332, 432],        # 25
[80, 120, 528, 432],        # 26
[80, 120, 725, 432],        # 27

############################# My Card Section
[80, 120, 58, 619],         # 28
[80, 120, 148, 619],        # 29
[80, 120, 238, 619],        # 30
[80, 120, 328, 619],        # 31
[80, 120, 418, 619],        # 32
[80, 120, 508, 619],        # 33
[80, 120, 598, 619],        # 34
[80, 120, 688, 619],        # 35
[80, 120, 778, 619],        # 36

############################# Interaction Section
[240, 364, 1051, 221],      # 37
[295, 110, 1051, 479],      # 38
[295, 110, 1051, 618],      # 39
]



class BoardLocation:
    def __init__(self, sectionNumber=0, width=0, height=0, centerX=0, centerY=0):
        self.sectionNumber = sectionNumber
        self.width = width
        self.height = height
        self.centerX = centerX
        self.centerY = centerY
        
class BoardEntity:
    def __init__(self, boardLocation=0, card = 0, player=0):
        self.boardLocation = boardLocation
        self.card = card
        self.palyer = player

class BoardSection:
    def __init__(self,player_list):
        self.boardSection = []
        self.player_list = player_list
        
        self.player_dict = {p:i for i,p in enumerate(player_list)}
        self.UI_dict = {}
        self.UI_dict[0] = [24,25,26,27,28,29,30,31,32,33,34,35,36]
        self.UI_dict[1] = [0,1,2,3,4,5]
        self.UI_dict[2] = [6,7,8,9,10,11]
        self.UI_dict[3] = [12,13,14,15,16,17]
        self.UI_dict[4] = [18,19,20,21,22,23]
        
        for index, temp in enumerate(BOARD_LIST):
            boardLocation = BoardLocation(index, temp[0], temp[1], temp[2], temp[3])
            boardEntity = BoardEntity(boardLocation, 0, 0)

            self.boardSection.append(boardEntity)

