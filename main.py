#main.py
#29th August 2021
#Nikolai Pesudovs
import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

WHITE = (255,255,255)
RED = (255,0,0)
def main():

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        WIN.fill((RED))
        pygame.display.update()

    pygame.QUIT()

if __name__ == "__main__":
    main()