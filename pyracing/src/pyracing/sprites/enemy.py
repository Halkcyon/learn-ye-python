import random

import pygame.sprite

from pyracing import ASSETS, SCREEN_HEIGHT, SCREEN_WIDTH, SPEED


class Enemy(pygame.sprite.Sprite):
    def __init__(self, *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)

        self.image = pygame.image.load(ASSETS / "Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def update(self):
        vert = (10 + SPEED) / 3

        self.rect.move_ip(0., vert)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
