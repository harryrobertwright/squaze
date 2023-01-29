from enum import Enum


class Direction(Enum):
    UP = (0, -5)
    DOWN = (0, 5)
    LEFT = (-5, 0)
    RIGHT = (5, 0)
