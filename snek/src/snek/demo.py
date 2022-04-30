import random
import sys

import pygame

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
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAY_SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self, *groups: pygame.sprite.AbstractGroup):
        super().__init__(*groups)

        self.image = pygame.image.load("Enemy.png").convert()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0., 10.)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)

        self.image = pygame.image.load("Player.png").convert()
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0 and pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5., 0.)

        if self.rect.right < SCREEN_WIDTH and pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5., 0.)

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
    E1.move()

    DISPLAY_SURFACE.fill(WHITE)
    P1.draw(DISPLAY_SURFACE)
    E1.draw(DISPLAY_SURFACE)

    pygame.display.update()
    FPS.tick(FRAMES_PER_SEC)
