import random
from dataclasses import dataclass, field
from colour import Colour
import pygame
from functools import cached_property


@dataclass
class Player:
    width: int = 35
    height: int = 35
    x_pos: int = 0
    y_pos: int = 845
    colour: Colour = Colour.BLACK

    @cached_property
    def rect(self):
        return pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)


@dataclass
class Obstacle:
    width: int = field(default_factory=lambda: random.randrange(25, 100, 5))
    height: int = field(default_factory=lambda: random.randrange(25, 100, 5))
    x_pos: int = field(default_factory=lambda: random.randrange(1, 1000, 5))
    y_pos: int = field(default_factory=lambda: random.randrange(1, 750, 5))
    colour: int = field(
        default_factory=lambda: (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
    )

    @cached_property
    def rect(self):
        return pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
