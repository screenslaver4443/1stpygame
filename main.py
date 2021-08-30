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
YELLOW = (255, 255, 0)

FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40 
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

BORDER = pygame.Rect(WIDTH//2-5, 0, 10, HEIGHT)

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
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            yellow_bullets.remove(bullet)

def draw_window(red, yellow, red_bullets, yellow_bullets):
    WIN.fill((WHITE))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.draw.rect(WIN, BLACK, BORDER)

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    red_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT and len(yellow_bullets)<MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x+yellow.width, yellow.y+yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet) 
                if event.key == pygame.K_RSHIFT and len(red_bullets)< MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y+red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, red_bullets, yellow_bullets)
    pygame.QUIT()

if __name__ == "__main__":
    main()