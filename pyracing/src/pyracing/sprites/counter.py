import pygame.sprite

from pyracing import SCREEN_WIDTH

from .number import Number


class Counter(pygame.sprite.Group):
    def __init__(self, counter=10):
        assert 0 < counter < 100  # 0 < counter and counter < 100

        self.counter = counter

        counter = f"{counter:02}"

        self.tens = Number(int(counter[0]))
        self.tens.rect.center = (SCREEN_WIDTH - 30 - 35, 35)

        self.ones = Number(int(counter[1]))
        super().__init__(self.tens, self.ones)

    def decrement(self):
        self.counter -= 1

        # 13 -> "13"
        # n[0] -> "1"
        # n[1] -> "3"
        # 1 -> "1"
        # n[0] -> 1
        # n[1] -> throw error
        counter = f"{self.counter:02}"
        tens = int(counter[0])
        ones = int(counter[1])

        self.tens.image = self.tens.image_list[tens % 10]
        self.ones.image = self.ones.image_list[ones % 10]
