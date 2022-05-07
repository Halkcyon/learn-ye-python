import pathlib
import random
import sys

import pygame

ROOT = pathlib.Path(__file__).resolve().parent
ASSETS = ROOT / "assets"

# initialize the framework
pygame.init()
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
SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pyracing")

# set up the game clock
FPS = 60
CLOCK = pygame.time.Clock()


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


class Counter(pygame.sprite.Group):
    def __init__(self):
        self.counter = 10

        self.tens = Number(1)
        self.tens.rect.center = (SCREEN_WIDTH - 30 - 35, 35)

        self.ones = Number(0)
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


P1 = Player()
E1 = Enemy()
COUNTER = Counter()

enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(COUNTER)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

connected = False

while True:
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                pygame.quit()
                sys.exit()

            case INC_SPEED:
                SPEED += 2

    SURFACE.fill(WHITE)
    for entity in all_sprites:
        SURFACE.blit(entity.image, entity.rect)
        entity.update()

    if pygame.sprite.spritecollideany(P1, enemies):
        if connected is False:
            COUNTER.decrement()
            connected = True

            if COUNTER.counter == 0:
                SURFACE.fill(RED)
                pygame.display.update()
                for entity in all_sprites:
                    entity.kill()

                import time
                time.sleep(2.)

                print("GAME OVER")
                pygame.quit()
                sys.exit()
    else:
        connected = False

    pygame.display.update()
    CLOCK.tick(FPS)
