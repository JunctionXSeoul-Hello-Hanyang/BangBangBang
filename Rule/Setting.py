# 플레이어의 수에 따른 직업의 수
# 보안관, 부관, 무법자, 배신자
NUMBER_OF_ROLE = {
    4: ['Sheriff', 'Outlaw', 'Outlaw', 'Renegade'],
    5: ['Sheriff', 'Deputy', 'Outlaw', 'Outlaw', 'Renegade'],
    6: ['Sheriff', 'Deputy', 'Outlaw', 'Outlaw', 'Outlaw', 'Renegade'],
    7: ['Sheriff', 'Deputy', 'Deputy', 'Outlaw', 'Outlaw', 'Outlaw', 'Renegade'],
}

# ConsumptionCard: 80
# H: Heart, D: Diamond, C, Clover, S: Space
PLAYING_CARD = [
    # ConsumptionCard: 63
    # Bang!: 25
    ['Bang!', 'Q', 'H', 'C'], ['Bang!', 'K', 'H', 'C'], ['Bang!', 'A', 'H', 'C'], ['Bang!', 'A', 'D', 'C'],
    ['Bang!', 'D', 'C', 'C'], ['Bang!', 'D', 'C', 'C'], ['Bang!', '4', 'D', 'C'], ['Bang!', '5', 'D', 'C'],
    ['Bang!', '6', 'D', 'C'], ['Bang!', '7', 'D', 'C'], ['Bang!', '8', 'D', 'C'], ['Bang!', '9', 'D', 'C'],
    ['Bang!', '10', 'D', 'C'], ['Bang!', 'J', 'D', 'C'], ['Bang!', 'Q', 'D', 'C'], ['Bang!', 'K', 'D', 'C'],
    ['Bang!', '2', 'C', 'C'], ['Bang!', '3', 'C', 'C'], ['Bang!', '4', 'C', 'C'], ['Bang!', '5', 'C', 'C'],
    ['Bang!', '6', 'C', 'C'], ['Bang!', '7', 'C', 'C'], ['Bang!', '8', 'C', 'C'],['Bang!', '9', 'C', 'C'],
    ['Bang!', 'A', 'S', 'C'],
    # Missed!: 12
    ['Missed!', '2', 'S', 'C'], ['Missed!', '3', 'S', 'C'], ['Missed!', '4', 'S', 'C'], ['Missed!', '5', 'S', 'C'],
    ['Missed!', '6', 'S', 'C'], ['Missed!', '7', 'S', 'C'], ['Missed!', '8', 'S', 'C'], ['Missed!', '10', 'C', 'C'],
    ['Missed!', 'J', 'C', 'C'], ['Missed!', 'K', 'C', 'C'], ['Missed!', 'A', 'C', 'C'], ['Missed!', 'Q', 'C', 'C'],
    # Beer: 6
    ['Beer', '6', 'H', 'C'], ['Beer', '7', 'H', 'C'], ['Beer', '8', 'H', 'C'], ['Beer', '9', 'H', 'C'],
    ['Beer', '10', 'H', 'C'], ['Beer', 'J', 'H', 'C'],
    # Duel: 3
    ['Duel', 'Q', 'D', 'C'], ['Duel', '8', 'C', 'C'], ['Duel', 'J', 'H', 'C'],
    # Indian!: 2
    ['Indian!', 'K', 'D', 'C'], ['Indian!', 'A', 'D', 'C'],
    # Gatling: 1
    ['Gatling', '10', 'H', 'C'],
    # Saloon: 1
    ['Saloon', '5', 'H', 'C'],
    # Panic!: 4
    ['Panic!', '8', 'D', 'C'], ['Panic!', 'J', 'H', 'C'], ['Panic!', 'Q', 'H', 'C'], ['Panic!', 'A', 'H', 'C'],
    # CatBalu: 4
    ['CatBalu', '9', 'D', 'C'], ['CatBalu', '10', 'D', 'C'], ['CatBalu', 'J', 'D', 'C'], ['CatBalu', 'K', 'H', 'C'],
    # GeneralStore: 2
    ['GeneralStore', '9', 'C', 'C'], ['GeneralStore', 'Q', 'H', 'C'],
    # Stagecoach: 2
    ['Stagecoach', '9', 'S', 'C'], ['Stagecoach', '9', 'S', 'C'],
    # WellsFargo: 1
    ['WellsFargo', '3', 'H', 'C'],

    # ConsumptionCard: 17
    # Gun: 8
    ['Schofield', 'J', 'C', 'E'], ['Schofield', 'Q', 'C', 'E'], ['Schofield', 'K', 'S', 'E'], ['Remington', 'A', 'C', 'E'],
    ['Remington', '5', 'S', 'E'], ['Winchester', '8', 'S', 'E'], ['Volcanic', '10', 'C', 'E'], ['Volcanic', '10', 'S', 'E'],
    # Jail: 3
    ['Jail', '4', 'H', 'E'], ['Jail', '10', 'S', 'E'], ['Jail', 'J', 'S', 'E'],
    # Barrel: 2
    ['Barrel', 'Q', 'S', 'E'], ['Barrel', 'K', 'S', 'E'],
    # Mustang: 2
    ['Mustang', '8', 'H', 'E'], ['Mustang', '9', 'H', 'E'],
    # Scope: 1
    ['WellsFargo', 'A', 'S', 'E'],
    # Dynamite: 1
    ['Dynamite', '2', 'H', 'E'],
]

IMAGES = {
    'Sheriff': None, 'Deputy': None, 'Outlaw': None, 'Outlaw': None, 'Renegade': None,

    'Bang!': None, 'Missed!': None, 'Beer': None, 'Duel': None, 'Indian!': None


    #...
}
