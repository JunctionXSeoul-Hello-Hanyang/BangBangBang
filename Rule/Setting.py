# 플레이어의 수에 따른 직업의 수
# 보안관, 부관, 무법자, 배신자
NUMBER_OF_ROLE = {
    4: ['sheriff', 'dutlaw', 'outlaw', 'renegade'],
    5: ['sheriff', 'deputy', 'outlaw', 'outlaw', 'renegade'],
    6: ['sheriff', 'deputy', 'outlaw', 'outlaw', 'outlaw', 'renegade'],
    7: ['sheriff', 'deputy', 'deputy', 'outlaw', 'outlaw', 'outlaw', 'renegade'],
}

# PlayingCard: 80
# H: Heart, D: Diamond, C, Clover, S: Space
PLAYING_CARD = [
    # ConsumptionCard: 63
    # bang: 25
    ['bang', 'Q', 'H', 'C'], ['bang', 'K', 'H', 'C'], ['bang', 'A', 'H', 'C'], ['bang', 'A', 'D', 'C'],
    ['bang', 'D', 'C', 'C'], ['bang', 'D', 'C', 'C'], ['bang', '4', 'D', 'C'], ['bang', '5', 'D', 'C'],
    ['bang', '6', 'D', 'C'], ['bang', '7', 'D', 'C'], ['bang', '8', 'D', 'C'], ['bang', '9', 'D', 'C'],
    ['bang', '10', 'D', 'C'], ['bang', 'J', 'D', 'C'], ['bang', 'Q', 'D', 'C'], ['bang', 'K', 'D', 'C'],
    ['bang', '2', 'C', 'C'], ['bang', '3', 'C', 'C'], ['bang', '4', 'C', 'C'], ['bang', '5', 'C', 'C'],
    ['bang', '6', 'C', 'C'], ['bang', '7', 'C', 'C'], ['bang', '8', 'C', 'C'],['bang', '9', 'C', 'C'],
    ['bang', 'A', 'S', 'C'],
    # missed: 12
    ['missed', '2', 'S', 'C'], ['missed', '3', 'S', 'C'], ['missed', '4', 'S', 'C'], ['missed', '5', 'S', 'C'],
    ['missed', '6', 'S', 'C'], ['missed', '7', 'S', 'C'], ['missed', '8', 'S', 'C'], ['missed', '10', 'C', 'C'],
    ['missed', 'J', 'C', 'C'], ['missed', 'K', 'C', 'C'], ['missed', 'A', 'C', 'C'], ['missed', 'Q', 'C', 'C'],
    # beer: 6
    ['beer', '6', 'H', 'C'], ['beer', '7', 'H', 'C'], ['beer', '8', 'H', 'C'], ['beer', '9', 'H', 'C'],
    ['beer', '10', 'H', 'C'], ['beer', 'J', 'H', 'C'],
    # duel: 3
    ['duel', 'Q', 'D', 'C'], ['duel', '8', 'C', 'C'], ['duel', 'J', 'H', 'C'],
    # indian!: 2
    ['indian', 'K', 'D', 'C'], ['indian', 'A', 'D', 'C'],
    # Gatling: 1
    ['gatling', '10', 'H', 'C'],
    # Saloon: 1
    ['saloon', '5', 'H', 'C'],
    # panic: 4
    ['panic', '8', 'D', 'C'], ['panic', 'J', 'H', 'C'], ['panic', 'Q', 'H', 'C'], ['panic', 'A', 'H', 'C'],
    # catBalu: 4
    ['catBalu', '9', 'D', 'C'], ['catBalu', '10', 'D', 'C'], ['catBalu', 'J', 'D', 'C'], ['catBalu', 'K', 'H', 'C'],
    # GeneralStore: 2
    ['generalStore', '9', 'C', 'C'], ['generalStore', 'Q', 'H', 'C'],
    # Stagecoach: 2
    ['stagecoach', '9', 'S', 'C'], ['stagecoach', '9', 'S', 'C'],
    # WellsFargo: 1
    ['wellsFargo', '3', 'H', 'C'],

    # ConsumptionCard: 17
    # Gun: 8
    ['schofield', 'J', 'C', 'EG'], ['schofield', 'Q', 'C', 'EG'], ['schofield', 'K', 'S', 'EG'], ['carabine', 'A', 'C', 'EG'],
    ['remington', '5', 'S', 'EG'], ['winchester', '8', 'S', 'EG'], ['volcanic', '10', 'C', 'EG'], ['volcanic', '10', 'S', 'EG'],
    # Jail: 3
    ['jail', '4', 'H', 'E'], ['jail', '10', 'S', 'E'], ['jail', 'J', 'S', 'E'],
    # Barrel: 2
    ['barrel', 'Q', 'S', 'E'], ['barrel', 'K', 'S', 'E'],
    # Mustang: 2
    ['mustang', '8', 'H', 'E'], ['mustang', '9', 'H', 'E'],
    # Scope: 1
    ['wellsFargo', 'A', 'S', 'E'],
    # Dynamite: 1
    ['dynamite', '2', 'H', 'E'],
]

GUN_RANGE = {'schofield':2, 'remington':3, 'winchester':5, 'volcanic':1, 'colt.45': 1, 'carabine':4}

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
