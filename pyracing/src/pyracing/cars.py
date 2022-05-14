import sys

import pygame

from . import *
from .sprites import *

# initialize the framework
pygame.init()

# set up the drawing surface
SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pyracing")

# fonts!
font = pygame.font.SysFont("Verdana", 60)
game_over = font.render("Game Over", True, BLACK)

# background!
background = pygame.image.load(ASSETS / "AnimatedStreet.png")

# sounds
crash = ASSETS / "crash.wav"
background_music = ASSETS / "background.wav"
pygame.mixer.music.load(background_music)
pygame.mixer.music.play(-1)

# set up the game clock
CLOCK = pygame.time.Clock()

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

    SURFACE.blit(background, (0, 0))
    for entity in all_sprites:
        SURFACE.blit(entity.image, entity.rect)
        entity.update()

    if pygame.sprite.spritecollideany(P1, enemies):
        if connected is False:
            pygame.mixer.Sound(crash).play()
            COUNTER.decrement()
            connected = True

            if COUNTER.counter == 0:
                SURFACE.fill(RED)
                SURFACE.blit(game_over, (30, 250))
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
