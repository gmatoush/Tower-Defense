import pygame as pg
import constants as c
from enemy import Enemy

# initialise pygame
pg.init()

# create clock
clock = pg.time.Clock()

# create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defense")

#load images
enemy_image = pg.image.load("assets/Gooby_Pixel.png").convert_alpha()

# create groups
enemy_group = pg.sprite.Group()

enemy = Enemy((200, 300), enemy_image)
enemy_group.add(enemy)

# game loop
run = True
while run:

    clock.tick(c.FPS)

    screen.fill("pink")

    # update groups
    enemy_group.update()

    # draw groups
    enemy_group.draw(screen)

    # event handler
    for event in pg.event.get():
        # quit program
        if event.type == pg.QUIT:
            run = False

    #update display
    pg.display.flip()

# quit pygame
pg.quit()