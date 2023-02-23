# SETUP PYGAME ZERO
import pygame

import pgzero

import pgzrun
# SCREEN
WIDTH = 800
HEIGHT = 600
# SETUP SCORE
score = 0

# SETUP Chappal
brick = Actor("brick")
brick.x = 90
brick.y = 250

# SETUP WALLS
wall_bottom = Actor("wall-bottom")
wall_top = Actor("wall-top")
gap = 150
wall_top.x = 300
wall_top.y = 0
wall_bottom.x = 300
wall_bottom.y = wall_top.height + gap


# BUTTON PRESSES
def on_mouse_down():
    print("The mouse has been clicked!")
    brick.y = brick.y - 50


# DRAW STUFF TO SCREEN
def draw():
    screen.fill("lightblue")
    brick.draw()
    wall_top.draw()
    wall_bottom.draw()
    screen.draw.text(str(score), (50, 30), color='orange')


# EACH CYCLE THROUGH THE LOOP
def update():
    global score

    brick.y = brick.y + 1
    wall_top.x = wall_top.x - 1
    wall_bottom.x = wall_bottom.x - 1
    # COLLISIONS
    if brick.colliderect(wall_top) or brick.colliderect(wall_bottom):
        reset()

    if brick.y > 600:
        reset()
    if wall_top.x < 0:
        reset_walls()
        score = score + 1


# RESET
def reset():
    global score
    print("the game is resetting!")
    brick.y = 250
    wall_bottom.x = 300
    wall_top.x = 300
    score = 0


def reset_walls():
    wall_bottom.x = 800
    wall_top.x = 800


# RUN PYGAME ZERO
pgzrun.go()