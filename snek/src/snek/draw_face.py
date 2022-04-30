import sys
import pygame
from pygame.locals import *

# initialize the framework
pygame.init()

# some useful color constants
BLUE = pygame.Color(0, 0, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

# set up our game clock
FPS = pygame.time.Clock()
FRAMES_PER_SEC = 30

# set up our drawing surface
DISPLAY_SURFACE = pygame.display.set_mode((300, 300))
DISPLAY_SURFACE.fill(WHITE)
pygame.display.set_caption("Hello!")

pygame.draw.line(DISPLAY_SURFACE, BLUE, (150, 130), (130, 170))
pygame.draw.line(DISPLAY_SURFACE, BLUE, (150, 130), (170, 170))
pygame.draw.line(DISPLAY_SURFACE, GREEN, (130, 170), (170, 170))
pygame.draw.circle(DISPLAY_SURFACE, BLACK, (100, 50), 30.)
pygame.draw.circle(DISPLAY_SURFACE, BLACK, (200, 50), 30.)
pygame.draw.rect(DISPLAY_SURFACE, RED, (100, 200, 100, 50), 2)
pygame.draw.rect(DISPLAY_SURFACE, BLACK, (110, 260, 80, 5))

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    FPS.tick(FRAMES_PER_SEC)
