from dataclasses import dataclass

import pygame

from colour import Colour
from objects.base import AbstractObject
from objects.coordinates import Coordinates
from objects.dimensions import Dimensions
from objects.obstacle import Obstacle


@dataclass
class Player(AbstractObject):
    dimensions: Dimensions = Dimensions(35, 35)
    coordinates: Coordinates = Coordinates(0, 865)
    colour: tuple[int, int, int] = Colour.BLACK
    index: int | None = None

    def get_obstacle_index_in_contact(self, obstacles: list[Obstacle]) -> int:
        for index, obstacle in enumerate(obstacles):
            offset_x = obstacle.rect.x - self.rect.x
            offset_y = obstacle.rect.y - self.rect.y

            if self.mask.overlap(obstacle.mask, (offset_x, offset_y)):
                return index

    def move(self, x: int, y: int) -> None:
        self.coordinates.x += x
        self.coordinates.y += y
        self.rect.x += x
        self.rect.y += y

    def check_collision(self, obstacles: list[Obstacle]) -> bool:
        index = self.get_obstacle_index_in_contact(obstacles)

        if index is not None:
            self.index = index
            return True

        self.index = None
        return False

    def constrain(self, constraint: pygame.Rect) -> None:
        self.rect.clamp_ip(constraint)

    def reset(self):
        self.rect.x, self.rect.x = self.coordinates.as_tuple()
