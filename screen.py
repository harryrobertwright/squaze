from colour import Colour
import pygame
from dataclasses import dataclass
from functools import cached_property

pygame.font.init()


@dataclass
class Screen:
    width: int = 1000
    height: int = 900
    background_colour: tuple[tuple[int, int, int]] = (Colour.WHITE.value,)
    font: pygame.font.Font = pygame.font.Font("fonts/OpenSans-Bold.ttf", 36)
    font_colour: tuple[int, int, int] = (Colour.BLACK.value,)
    clock: pygame.time.Clock = pygame.time.Clock()
    clock_tick: int = 60

    @cached_property
    def screen(self):
        return pygame.display.set_mode((self.width, self.height))

    def refresh_background(self):
        """Fills the screen with the background colour"""
        self.screen.fill(self.background_colour)

    def draw_obstacles(self, obstacles):
        for obstacle in obstacles:
            pygame.draw.rect(self.screen, obstacle.colour, obstacle.rect)

    def draw_player(self, player):
        pygame.draw.rect(self.screen, player.colour.value, player.rect)

    def draw_round(self, round):
        text = self.font.render(f"Round: {round}", True, self.font_colour)
        self.screen.blit(text, (800, 850))

    def update_screen(self, player, obstacles, round):
        self.refresh_background()
        self.draw_obstacles(obstacles)
        self.draw_player(player)
        self.draw_round(round)
        self.clock.tick(self.clock_tick)
        pygame.display.update()
