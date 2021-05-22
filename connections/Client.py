import pygame
from Network import Network

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
clientNumber = 0





if __name__ == "__main__":
    run = True
    network = Network("18.191.254.252", 5555)
    clock = pygame.time.Clock()
    clock.tick(60)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                network.close()
                print('Quit')


