#main.py
#29th August 2021
#Nikolai Pesudovs
import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

WHITE = (255,255,255)
RED = (255,0,0)

FPS = 60

def draw_window():
    WIN.fill((RED))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window()
    pygame.QUIT()

if __name__ == "__main__":
    main()