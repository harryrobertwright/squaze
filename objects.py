import random
from abc import ABC
from dataclasses import dataclass
from dataclasses import field
from functools import cached_property

import pygame

from colour import Colour


@dataclass
class Coordinates:
    x: int
    y: int

    @classmethod
    def random(cls) -> "Coordinates":
        return Coordinates(random.randrange(1, 1000, 5), random.randrange(1, 750, 5))


@dataclass
class Dimensions:
    width: int
    height: int

    @classmethod
    def random(cls) -> "Dimensions":
        return cls(random.randrange(25, 100, 5), random.randrange(25, 100, 5))


class AbstractObject(ABC):
    dimensions: Dimensions
    coordinates: Coordinates

    @cached_property
    def rect(self):
        return pygame.Rect(
            self.coordinates.x,
            self.coordinates.y,
            self.dimensions.width,
            self.dimensions.height,
            border_radius=0,
        )


@dataclass
class Player(AbstractObject):
    dimensions: Dimensions = Dimensions(35, 35)
    coordinates: Coordinates = Coordinates(0, 845)
    colour: Colour = Colour.BLACK


@dataclass
class Obstacle(AbstractObject):
    dimensions: Dimensions = field(default_factory=Dimensions.random)
    coordinates: Coordinates = field(default_factory=Coordinates.random)
    colour: int = field(
        default_factory=lambda: (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
    )

    @classmethod
    def create_batch(cls, size: int) -> list["Obstacle"]:
        obstacles = []
        for _ in range(size):
            obstacle = Obstacle()
            if (
                obstacle.rect.collidelist([obstacle.rect for obstacle in obstacles])
                == -1
            ):
                obstacles.append(obstacle)

        return obstacles
