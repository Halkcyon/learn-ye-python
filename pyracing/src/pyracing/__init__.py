"""https://www.pygame.org/docs/"""

__all__ = [
    "ASSETS",
    "SPEED",
    "WHITE",
    "BLUE",
    "RED",
    "GREEN",
    "BLACK",
    "SCREEN_WIDTH",
    "SCREEN_HEIGHT",
    "FPS",
]
__version__ = '0.1.0'

import pathlib

import pygame

ROOT = pathlib.Path(__file__).resolve().parent
ASSETS = ROOT / "assets"

SPEED = 5

# https://www.pygame.org/docs/ref/color_list.html
WHITE = pygame.Color(255, 255, 255)
BLUE = pygame.Color("blue")
RED = pygame.Color("red")
GREEN = pygame.Color("green")
BLACK = pygame.Color("black")

# set up the drawing surface
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# set up the game clock
FPS = 60
