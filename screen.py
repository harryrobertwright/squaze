from dataclasses import dataclass
from functools import cached_property

import pygame

from colour import Colour
from objects import Dimensions

pygame.font.init()


@dataclass
class Clock:
    instance: pygame.time.Clock = pygame.time.Clock()
    frame_rate: int = 60

    def tick(self):
        return self.instance.tick(self.frame_rate)


@dataclass
class Font:
    instance: pygame.font.Font = pygame.font.Font("fonts/OpenSans-Bold.ttf", 36)
    colour: tuple[int, int, int] = (Colour.BLACK.value,)

    def render(self, text: str):
        return self.instance.render(text, True, self.colour)


@dataclass
class Screen:
    dimensions: Dimensions = Dimensions(1000, 900)
    background_colour: tuple[tuple[int, int, int]] = (Colour.WHITE.value,)
    font: Font = Font()
    clock: Clock = Clock()

    @cached_property
    def instance(self):
        return pygame.display.set_mode((self.dimensions.width, self.dimensions.height))

    def refresh_background(self):
        """Fills the screen with the background colour"""
        self.instance.fill(self.background_colour)

    def draw_obstacles(self, obstacles):
        for obstacle in obstacles:
            pygame.draw.rect(self.instance, obstacle.colour, obstacle.rect)

    def draw_player(self, player):
        pygame.draw.rect(self.instance, player.colour.value, player.rect)

    def draw_round(self, round):
        text = self.font.render(f"Round: {round}")
        self.instance.blit(text, (800, 850))

    def update(self, player, obstacles, round):
        self.refresh_background()
        self.draw_obstacles(obstacles)
        self.draw_player(player)
        self.draw_round(round)
        self.clock.tick()
        pygame.display.update()
