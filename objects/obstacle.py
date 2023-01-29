import random
from dataclasses import dataclass
from dataclasses import field
from enum import Enum

from objects.base import AbstractObject
from objects.coordinates import Coordinates
from objects.dimensions import Dimensions


class Direction(Enum):
    UP = (0, -5)
    DOWN = (0, 5)
    LEFT = (-5, 0)
    RIGHT = (5, 0)


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

        while len(obstacles) != size:
            obstacle = Obstacle()
            rects = [obstacle.rect for obstacle in obstacles]
            if obstacle.rect.collidelist(rects) == -1:
                obstacles.append(obstacle)

        return obstacles
