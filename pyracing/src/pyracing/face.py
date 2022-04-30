import sys

import pygame

# initialize the framework
pygame.init()

# https://www.pygame.org/docs/ref/color_list.html
WHITE = pygame.Color(255, 255, 255)
BLUE = pygame.Color("blue")
RED = pygame.Color("red")
GREEN = pygame.Color("green")
BLACK = pygame.Color("black")

# set up the drawing surface
SURFACE = pygame.display.set_mode((300, 300))
pygame.display.set_caption("hello!")

# set up the game clock
FPS = 30
CLOCK = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SURFACE.fill(WHITE)

    pygame.draw.line(SURFACE, BLUE, (150, 130), (130, 170), 2)
    pygame.draw.line(SURFACE, BLUE, (150, 130), (170, 170), 2)
    pygame.draw.line(SURFACE, GREEN, (130, 170), (170, 170), 2)

    pygame.draw.circle(SURFACE, BLACK, (100, 50), 30.)
    pygame.draw.circle(SURFACE, BLACK, (200, 50), 30.)

    pygame.draw.rect(SURFACE, RED, (100, 200, 100, 50), 2)
    pygame.draw.rect(SURFACE, BLACK, (110, 260, 80, 5))

    pygame.display.update()
    CLOCK.tick(FPS)
