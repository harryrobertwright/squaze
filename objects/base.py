from abc import ABC
from functools import cached_property

import pygame

from colour import Colour
from objects.coordinates import Coordinates
from objects.dimensions import Dimensions


class AbstractObject(ABC):
    dimensions: Dimensions
    coordinates: Coordinates
    colour: Colour

    @cached_property
    def surface(self) -> pygame.Surface:
        surface = pygame.Surface(self.dimensions.as_tuple())
        surface.fill(self.colour)

        return surface

    @cached_property
    def rect(self):
        return self.surface.get_rect(**self.coordinates.as_dict())

    @cached_property
    def mask(self):
        return pygame.mask.from_surface(self.surface)
