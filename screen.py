from colour import Colour
import pygame
from pygame.locals import *
import math

class Screen:
    def __init__(self, WIDTH=1000, HEIGHT=900, background_colour=Colour.WHITE, font_type='fonts/OpenSans-Bold.ttf', font_dimensions=36, font_colour=Colour.BLACK, clock_tick=60):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.background_colour = background_colour
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font = pygame.font.Font(font_type, font_dimensions)
        self.font_colour = font_colour
        self.clock = pygame.time.Clock()
        self.clock_tick = clock_tick

    def refresh_background(self):
        """Fills the screen with the background colour"""
        self.screen.fill(self.background_colour)

    def draw_obstacles(self, obstacles):
        for obstacle in obstacles:
            pygame.draw.rect(self.screen, obstacle.colour, obstacle.rect)

    def draw_player(self, player):
        pygame.draw.rect(self.screen, player.colour, player.rect)

    def draw_round(self, round):
        text = self.font.render(f'Round: {round}', True, self.font_colour)
        self.screen.blit(text, (800, 850))


    def update_screen(self, player, obstacles, round):
        self.refresh_background()
        self.draw_obstacles(obstacles)
        self.draw_player(player)
        self.draw_round(round)
        self.clock.tick(self.clock_tick)
        pygame.display.update()
