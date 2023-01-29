from dataclasses import dataclass
from functools import cached_property

import orm_sqlite
import pygame

from colour import Colour
from models import Score
from objects import AbstractObject
from objects import Dimensions
from objects import Obstacle
from objects import Player

db = orm_sqlite.Database("example.db")
Score.objects.backend = db

pygame.font.init()


@dataclass
class Clock:
    instance: pygame.time.Clock = pygame.time.Clock()
    frame_rate: int = 60

    def tick(self):
        return self.instance.tick(self.frame_rate)


@dataclass
class Font:
    instance: pygame.font.Font = pygame.font.Font("fonts/upheavtt.ttf", 36)
    colour: tuple[int, int, int] = (Colour.BLACK,)

    def render(self, text: str):
        return self.instance.render(text, True, self.colour)


@dataclass
class Screen:
    dimensions: Dimensions = Dimensions(1000, 900)
    background_colour: tuple[tuple[int, int, int]] = (Colour.WHITE,)
    font: Font = Font()
    clock: Clock = Clock()

    @cached_property
    def instance(self):
        return pygame.display.set_mode((self.dimensions.width, self.dimensions.height))

    def _refresh_background(self) -> None:
        """Fills the screen with the background colour"""
        self.instance.fill(self.background_colour)

    def _draw(self, obj: AbstractObject) -> None:
        pygame.draw.rect(self.instance, obj.colour, obj.rect)

    def _draw_obstacles(self, obstacles: list[Obstacle]) -> None:
        for obstacle in obstacles:
            self._draw(obstacle)

    def _draw_player(self, player: Player) -> None:
        player.constrain(self.instance.get_rect())
        self._draw(player)

    def _draw_round(self, round: int, bombs: int) -> None:
        high_score = next(
            iter(
                sorted((score["value"] for score in Score.objects.all()), reverse=True)
            ),
            "N/A",
        )

        strings = (f"Round: {round}", f"Bombs: {bombs}", f"High score: {high_score}")
        dimensions_array = (
            Dimensions(800, 850),
            Dimensions(550, 850),
            Dimensions(150, 850),
        )

        for string, dimensions in zip(strings, dimensions_array):
            text = self.font.render(string)
            self.instance.blit(text, dimensions.as_tuple())

    def update(self, player: Player, obstacles: list[Obstacle], round: int, bombs: int):
        self._refresh_background()
        self._draw_obstacles(obstacles)
        self._draw_player(player)
        self._draw_round(round, bombs)
        self.clock.tick()
        pygame.display.update()
