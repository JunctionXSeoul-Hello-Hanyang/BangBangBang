# 플레이어의 수에 따른 직업의 수
# 보안관, 부관, 무법자, 배신자
NUMBER_OF_ROLE = {
    4: ['Sheriff', 'Outlaw', 'Outlaw', 'Renegade'],
    5: ['Sheriff', 'Deputy', 'Outlaw', 'Outlaw', 'Renegade'],
    6: ['Sheriff', 'Deputy', 'Outlaw', 'Outlaw', 'Outlaw', 'Renegade'],
    7: ['Sheriff', 'Deputy', 'Deputy', 'Outlaw', 'Outlaw', 'Outlaw', 'Renegade'],
}

# PlayingCard: 80
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
    ['Schofield', 'J', 'C', 'EG'], ['Schofield', 'Q', 'C', 'EG'], ['Schofield', 'K', 'S', 'EG'], ['Remington', 'A', 'C', 'EG'],
    ['Remington', '5', 'S', 'EG'], ['Winchester', '8', 'S', 'EG'], ['Volcanic', '10', 'C', 'EG'], ['Volcanic', '10', 'S', 'EG'],
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

IMAGE_ROLE_PATH = '../UI/ImageAsset/roles/'
IMAGE_PLAYINGCARD_PATH = '../UI/ImageAsset/cards/'

IMAGES = {
    # Roles
    'Sheriff': IMAGE_ROLE_PATH + 'sheriff.png', 
    'Deputy': IMAGE_ROLE_PATH + 'deputy.png', 
    'Outlaw': IMAGE_ROLE_PATH + 'outlaw.png', 
    'Renegade': IMAGE_ROLE_PATH + 'renegade.png',

    # Characters

    # Playing Cards
    # Weapon
    'appaloosa': IMAGE_PLAYINGCARD_PATH + 'appaloosa.png', 
    'carabine': IMAGE_PLAYINGCARD_PATH + 'carabine.png',
    'mustang.png' : IMAGE_PLAYINGCARD_PATH + 'mustang.png',
    'remington.png' : IMAGE_PLAYINGCARD_PATH + 'remington.png',
    'schofield.png' : IMAGE_PLAYINGCARD_PATH + 'schofield.png',
    'volcanic.png' : IMAGE_PLAYINGCARD_PATH + 'volcanic.png',
    'winchester.png' : IMAGE_PLAYINGCARD_PATH + 'winchester.png',

    # Equipment
    'Barrel': IMAGE_PLAYINGCARD_PATH + 'barrel.png', 
    'Dynamite': IMAGE_PLAYINGCARD_PATH + 'dynamite.png', 
    'Jail.png' : IMAGE_PLAYINGCARD_PATH + 'jail.png',

    # Consumption
    'bang': IMAGE_PLAYINGCARD_PATH + 'bang.png', 
    'beer': IMAGE_PLAYINGCARD_PATH + 'beer.png', 
    'carabine': IMAGE_PLAYINGCARD_PATH + 'carabine.png',
    'diligenza.png' : IMAGE_PLAYINGCARD_PATH + 'diligenza.png',
    'duel.png' : IMAGE_PLAYINGCARD_PATH + 'duel.png',
    'gatling.png' : IMAGE_PLAYINGCARD_PATH + 'gatling.png',
    'indians.png' : IMAGE_PLAYINGCARD_PATH + 'indians.png',
    'missed.png' : IMAGE_PLAYINGCARD_PATH + 'missed.png',
    'panico.png' : IMAGE_PLAYINGCARD_PATH + 'panico.png',
    'saloon.png' : IMAGE_PLAYINGCARD_PATH + 'saloon.png',
    'wellsfargo.png' : IMAGE_PLAYINGCARD_PATH + 'wellsfargo.png',

    #...
}
