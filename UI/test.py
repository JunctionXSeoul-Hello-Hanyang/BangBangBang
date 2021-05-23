def update_player(self, player):
    index = self.board.player_dict[player.player_number]
    if index == 0:
        self.update_card(self.board.UI_dict[index][0], Card(player.field.role, 0, 0, 0, 0))  # not yet
        self.update_card(self.board.UI_dict[index][1], player.field.equipmentCards)
        self.update_card(self.board.UI_dict[index][2], player.field.gunCard)
        self.update_card(self.board.UI_dict[index][3], Card(str(player.field.bullets), 0, 0, 0, 0))
        for i, card in enumerate(player.cards):
            self.update_card(self.board.UI_dict[index][4 + i], card)
    else:
        self.update_card(self.board.UI_dict[index][0], Card(str("Player" + str(player.player_number)), 0, 0, 0, 0))
        self.update_card(self.board.UI_dict[index][1], Card(player.field.role, 0, 0, 0, 0))
        self.update_card(self.board.UI_dict[index][2], player.field.equipmentCards)
        self.update_card(self.board.UI_dict[index][3], Card(str(len(player.cards)), 0, 0, 0, 0))
        self.update_card(self.board.UI_dict[index][4], player.field.gunCard)
        self.update_card(self.board.UI_dict[index][5], Card(str(player.field.bullets), 0, 0, 0, 0))


12: 57
if player.field.role == "sheriff":
    self.update_card(self.board.UI_dict[index][1], Card(player.field.role, 0, 0, 0, 0))
else:
    self.update_card(self.board.UI_dict[index][1], Card("ROLE_UNKNOWN", 0, 0, 0, 0))
12: 57
if player.field.role == "sheriff":
    self.update_card(self.board.UI_dict[index][1], Card(player.field.role, 0, 0, 0, 0)) else:
    self.update_card(self.board.UI_dict[index][1], Card("ROLE_UNKNOWN", 0, 0, 0, 0))
12: 58
if player.field.role == "sheriff":
    self.update_card(self.board.UI_dict[index][1], Card(player.field.role, 0, 0, 0, 0))
else:
    self.update_card(self.board.UI_dict[index][1], Card("ROLE_UNKNOWN", 0, 0, 0, 0))
12: 58
아니
다시적을께
12: 58
if player.field.role == "sheriff":
    self.update_card(self.board.UI_dict[index][1], Card(player.field.role, 0, 0, 0, 0))
else:
    self.update_card(self.board.UI_dict[index][1], Card("ROLE_UNKNOWN", 0, 0, 0, 0))
12: 58


def update_player(self, player):
    index = self.board.player_dict[player.player_number]
    if index == 0:
        self.update_card(self.board.UI_dict[index][0], Card(player.field.role, 0, 0, 0, 0))  # not yet
        self.update_card(self.board.UI_dict[index][1], player.field.equipmentCards)
        self.update_card(self.board.UI_dict[index][2], player.field.gunCard)
        self.update_card(self.board.UI_dict[index][3], Card(str(player.field.bullets), 0, 0, 0, 0))
        for i, card in enumerate(player.cards):
            self.update_card(self.board.UI_dict[index][4 + i], card)
    else:
        self.update_card(self.board.UI_dict[index][0], Card(str("Player" + str(player.player_number)), 0, 0, 0, 0))
        if player.field.role == "sheriff":
            self.update_card(self.board.UI_dict[index][1], Card(player.field.role, 0, 0, 0, 0))
        else:
            self.update_card(self.board.UI_dict[index][1], Card("ROLE_UNKNOWN", 0, 0, 0, 0))
        self.update_card(self.board.UI_dict[index][2], player.field.equipmentCards)
        self.update_card(self.board.UI_dict[index][3], Card(str(len(player.cards)), 0, 0, 0, 0))
        self.update_card(self.board.UI_dict[index][4], player.field.gunCard)
        self.update_card(self.board.UI_dict[index][5], Card(str(player.field.bullets), 0, 0, 0, 0))