import sys

import pygame

from constants import Direction
from game import Game
from screen import Screen

pygame.init()


screen = Screen()
game = Game()


pygame.time.get_ticks()

while True:

    game.new_round()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        game.move_player(Direction.UP)

    if keys[pygame.K_DOWN]:
        game.move_player(Direction.DOWN)

    if keys[pygame.K_LEFT]:
        game.move_player(Direction.LEFT)

    if keys[pygame.K_RIGHT]:
        game.move_player(Direction.RIGHT)

    if keys[pygame.K_SPACE]:
        game.destroy_obstacles()

    screen.update(game.player, game.obstacles, game.round, game.bombs)
