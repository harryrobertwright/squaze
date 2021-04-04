import sys
import pygame
from screen import Screen
from game import Game

pygame.init()

screen = Screen()
game = Game()

run = True


start_ticks = pygame.time.get_ticks() #starter tick

while run:
    
    game.new_round()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        game.update_player_pos(y_pos=-5)

    if keys[pygame.K_DOWN]:
        game.update_player_pos(y_pos=5)

    if keys[pygame.K_LEFT]:
        game.update_player_pos(x_pos=-5)

    if keys[pygame.K_RIGHT]:
        game.update_player_pos(x_pos=5)


    screen.update_screen(game.player, game.obstacles, game.round)
