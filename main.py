#main.py
#29th August 2021
#Nikolai Pesudovs
import pygame
import os

pygame.init()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0, 0, 0)

FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40 
VEL = 5
BORDER = pygame.Rect(WIDTH/2-5, 0, 10, HEIGHT)

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.bmp'))

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.bmp'))

RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def yellow_handle_movement(keys_pressed, yellow):
        if keys_pressed[pygame.K_a] and yellow.x-VEL>0: #yellow player to Left
            yellow.x -= VEL
        if keys_pressed[pygame.K_d] and yellow.x-VEL + yellow.width <BORDER.x: #yellow player to Right
            yellow.x += VEL
        if keys_pressed[pygame.K_w] and yellow.y-VEL > 0: #yellow player to Up
            yellow.y -= VEL
        if keys_pressed[pygame.K_s] and yellow.y-VEL + yellow.height < HEIGHT-15: #yellow player to Down
            yellow.y += VEL
            
def red_handle_movement(keys_pressed, red): #Red Player Movement
        if keys_pressed[pygame.K_LEFT] and red.x-VEL> BORDER.x + BORDER.width: #red player to Left
            red.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and red.x-VEL+red.width < WIDTH: #red player to Right
            red.x += VEL
        if keys_pressed[pygame.K_UP] and red.y-VEL > 0 : #red player to Up
            red.y -= VEL
        if keys_pressed[pygame.K_DOWN] and red.y-VEL+ red.height < HEIGHT-15: #red player to Down
            red.y += VEL

def draw_window(red, yellow):
    WIN.fill((WHITE))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.draw.rect(WIN, BLACK, BORDER)
    pygame.display.update()

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)
    pygame.QUIT()

if __name__ == "__main__":
    main()