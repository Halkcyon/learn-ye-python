import pygame.sprite

from pyracing import ASSETS, SCREEN_WIDTH


class Number(pygame.sprite.Sprite):
    def __init__(self, start: int, *groups: pygame.sprite.AbstractGroup):
        super().__init__(*groups)

        self.image_list = [
            pygame.image.load(ASSETS / "0.png"),
            pygame.image.load(ASSETS / "1.png"),
            pygame.image.load(ASSETS / "2.png"),
            pygame.image.load(ASSETS / "3.png"),
            pygame.image.load(ASSETS / "4.png"),
            pygame.image.load(ASSETS / "5.png"),
            pygame.image.load(ASSETS / "6.png"),
            pygame.image.load(ASSETS / "7.png"),
            pygame.image.load(ASSETS / "8.png"),
            pygame.image.load(ASSETS / "9.png"),
        ]

        self.image = self.image_list[start]
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH - 30, 35)
