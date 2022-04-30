import pathlib
import random
import sys

import pygame

ROOT = pathlib.Path(__file__).resolve().parent
ASSETS = ROOT / "assets"

# initialize the framework
pygame.init()

# https://www.pygame.org/docs/ref/color_list.html
WHITE = pygame.Color(255, 255, 255)
BLUE = pygame.Color("blue")
RED = pygame.Color("red")
GREEN = pygame.Color("green")
BLACK = pygame.Color("black")

# set up the drawing surface
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pyracing")

# set up the game clock
FPS = 60
CLOCK = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups: pygame.sprite.AbstractGroup):
        super().__init__(*groups)

        self.image = pygame.image.load(ASSETS / "Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5., 0.)

        if pressed_keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5., 0.)

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)

        self.image = pygame.image.load(ASSETS / "Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def update(self):
        self.rect.move_ip(0., 10.)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)


P1 = Player()
E1 = Enemy()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.update()

    SURFACE.fill(WHITE)
    P1.draw(SURFACE)
    E1.draw(SURFACE)

    pygame.display.update()
    CLOCK.tick(FPS)
