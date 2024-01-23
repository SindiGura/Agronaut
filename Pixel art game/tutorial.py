
import pygame, sys


#Setting up the screen and clock
pygame.init()
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


#Setting up the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')

    pygame.display.update()
    clock.tick(60)

