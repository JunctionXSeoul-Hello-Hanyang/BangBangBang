# 플레이어의 수에 따른 직업의 수
# 보안관, 부관, 무법자, 배신자
NUMBER_OF_CHARACTER = {
    4: {'Sheriff': 1, 'Deputy': 0, 'Outlaw': 2, 'Renegade': 1},
    5: {'Sheriff': 1, 'Deputy': 1, 'Outlaw': 2, 'Renegade': 1},
    6: {'Sheriff': 1, 'Deputy': 1, 'Outlaw': 3, 'Renegade': 1},
    7: {'Sheriff': 1, 'Deputy': 2, 'Outlaw': 3, 'Renegade': 1},
}

# PlayingCard: 80
# H: Heart, D: Diamond, C, Clover, S: Space
PLAYING_CARD = [
    # ConsumptionCard: 63
    # Bang!: 25
    ['Bang!', 'Q', 'H'], ['Bang!', 'K', 'H'], ['Bang!', 'A', 'H'], ['Bang!', 'A', 'D'],
    ['Bang!', 'D', 'C'], ['Bang!', 'D', 'C'], ['Bang!', '4', 'D'], ['Bang!', '5', 'D'],
    ['Bang!', '6', 'D'], ['Bang!', '7', 'D'], ['Bang!', '8', 'D'], ['Bang!', '9', 'D'],
    ['Bang!', '10', 'D'], ['Bang!', 'J', 'D'], ['Bang!', 'Q', 'D'], ['Bang!', 'K', 'D'],
    ['Bang!', '2', 'C'], ['Bang!', '3', 'C'], ['Bang!', '4', 'C'], ['Bang!', '5', 'C'],
    ['Bang!', '6', 'C'], ['Bang!', '7', 'C'], ['Bang!', '8', 'C'],['Bang!', '9', 'C'],
    ['Bang!', 'A', 'S'],
    # Missed!: 12
    ['Missed!', '2', 'S'], ['Missed!', '3', 'S'], ['Missed!', '4', 'S'], ['Missed!', '5', 'S'],
    ['Missed!', '6', 'S'], ['Missed!', '7', 'S'], ['Missed!', '8', 'S'], ['Missed!', '10', 'C'],
    ['Missed!', 'J', 'C'], ['Missed!', 'K', 'C'], ['Missed!', 'A', 'C'], ['Missed!', 'Q', 'C'],
    # Beer: 6
    ['Beer', '6', 'H'], ['Beer', '7', 'H'], ['Beer', '8', 'H'], ['Beer', '9', 'H'],
    ['Beer', '10', 'H'], ['Beer', 'J', 'H'],
    # Duel: 3
    ['Duel', 'Q', 'D'], ['Duel', '8', 'C'], ['Duel', 'J', 'H'],
    # Indian!: 2
    ['Indian!', 'K', 'D'], ['Indian!', 'A', 'D'],
    # Gatling: 1
    ['Gatling', '10', 'H'],
    # Saloon: 1
    ['Saloon', '5', 'H'],
    # Panic!: 4
    ['Panic!', '8', 'D'], ['Panic!', 'J', 'H'], ['Panic!', 'Q', 'H'], ['Panic!', 'A', 'H'],
    # CatBalu: 4
    ['CatBalu', '9', 'D'], ['CatBalu', '10', 'D'], ['CatBalu', 'J', 'D'], ['CatBalu', 'K', 'H'],
    # GeneralStore: 2
    ['GeneralStore', '9', 'C'], ['GeneralStore', 'Q', 'H'],
    # Stagecoach: 2
    ['Stagecoach', '9', 'S'], ['Stagecoach', '9', 'S'],
    # WellsFargo: 1
    ['WellsFargo', '3', 'H'],

    # ConsumptionCard: 17
    # Gun: 8
    ['Schofield', 'J', 'C'], ['Schofield', 'Q', 'C'], ['Schofield', 'K', 'S'], ['Remington', 'A', 'C'],
    ['Remington', '5', 'S'], ['Winchester', '8', 'S'], ['Volcanic', '10', 'C'], ['Volcanic', '10', 'S'],
    # Jail: 3
    ['Jail', '4', 'H'], ['Jail', '10', 'S'], ['Jail', 'J', 'S'],
    # Barrel: 2
    ['Barrel', 'Q', 'S'], ['Barrel', 'K', 'S'],
    # Mustang: 2
    ['Mustang', '8', 'H'], ['Mustang', '9', 'H'],
    # Scope: 1
    ['WellsFargo', 'A', 'S'],
    # Dynamite: 1
    ['Dynamite', '2', 'H'],
]

