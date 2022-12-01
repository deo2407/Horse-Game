import pygame as pg
from pygame.locals import *
import os
import random

pg.init()

WIDTH, HEIGHT = 1280, 640
BLACK = (20, 20, 20)
WHITE = (250, 250, 250)

FONT = pg.font.SysFont(None, 40)

VEL = 6
FPS = 60

APPLE_EATEN = pg.USEREVENT + 1  # * creating an unique event


class Hero:  # TODO
    def __init__(self):
        self.width = 50
        self.height = 40


def load_img(name):
    path_name = os.path.join("Assets", name)

    image = pg.image.load(path_name)
    image.convert()
    pg.transform.scale(image, (10, 10))

    image_rect = image.get_rect()

    return image, image_rect


def handle_movement(key_pressed, hero):
    if key_pressed[pg.K_d]:
        hero.x += VEL

    if key_pressed[pg.K_a]:
        hero.x -= VEL

    if key_pressed[pg.K_s]:
        hero.y += VEL

    if key_pressed[pg.K_w]:
        hero.y -= VEL


def handle_collision(hero, apple):
    if hero.colliderect(apple):
        pg.event.post(pg.event.Event(APPLE_EATEN))


def win(apples_eaten, WIN):
    if apples_eaten == 8:
        win_text = FONT.render("You win!", 1, WHITE)
        WIN.blit(win_text, (WIDTH/2 - win_text.get_width() /
                 2, HEIGHT / 2 - win_text.get_height() / 2))

        pg.display.update()
        pg.time.delay(4000)
        pg.quit()


def handle_text(apples_eaten):
    text = FONT.render(f"Apples: {apples_eaten}", 1, WHITE)
    textpos = text.get_rect()
    textpos.x, textpos.y = 10, 10

    return text, textpos


def main():
    clock = pg.time.Clock()
    apples_eaten = 0

    WIN = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Horse Game")

    BACKGROUND = pg.Surface(WIN.get_size())
    BACKGROUND.convert()
    BACKGROUND.fill(BLACK)

    hero_img, hero = load_img("Untitled-2.png")
    hero.x, hero.y = WIN.get_width() / 2 - 25, WIN.get_height() / 2 - 20

    apple_img, apple = load_img("Untitled-1.png")
    apple.x, apple.y = random.randrange(0, WIDTH), random.randrange(0, HEIGHT)

    while True:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == QUIT:
                return

            if event.type == APPLE_EATEN:
                apple.x, apple.y = random.randrange(
                    0, WIDTH), random.randrange(0, HEIGHT)

                apples_eaten += 1

        WIN.blit(BACKGROUND, (0, 0))

        WIN.blit(apple_img, (apple.x, apple.y))
        WIN.blit(hero_img, (hero.x, hero.y))

        text, textpos = handle_text(apples_eaten)
        WIN.blit(text, textpos)

        key_pressed = pg.key.get_pressed()
        handle_movement(key_pressed, hero)

        handle_collision(hero, apple)

        win(apples_eaten, WIN)

        pg.display.flip()


if __name__ == "__main__":
    main()
