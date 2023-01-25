from dataclasses import dataclass
from dataclasses import field

import pygame

from objects import Obstacle
from objects import Player
from screen import Screen


@dataclass
class Game:
    obstacles: list = field(default_factory=list)
    player: Player = Player()
    round: int = 0
    screen: Screen = Screen()

    def check_collision(self, test_rect):
        tolerance = 1

        return any(
            test_rect.colliderect(tuple(obstacle.rect[i] - tolerance for i in range(4)))
            for obstacle in self.obstacles
        )

    def boundary_check(self, test_rect):
        return 0 <= test_rect[0] < (
            self.screen.dimensions.width - test_rect[2]
        ) and 0 <= test_rect[1] < (self.screen.dimensions.height - test_rect[3])

    def round_completed(self):
        return self.player.coordinates.y - self.player.dimensions.height <= 0

    def update_player_pos(self, x_pos=0, y_pos=0):
        test_rect = pygame.Rect(
            self.player.coordinates.x + x_pos,
            self.player.coordinates.y + y_pos,
            self.player.dimensions.width,
            self.player.dimensions.height,
        )
        if not self.check_collision(test_rect) and self.boundary_check(test_rect):
            self.player.coordinates.x += x_pos
            self.player.coordinates.y += y_pos
            self.player.rect = test_rect

    def spawn_obstacles(self):
        size = self.get_difficulty()
        obstacles = Obstacle.create_batch(size)
        self.obstacles.extend(obstacles)

    def get_difficulty(self):
        return self.round * 10

    def new_round(self):
        if not self.obstacles:
            self.round += 1
            self.spawn_obstacles()

        if self.round_completed():
            self.player.coordinates.x = 0
            self.player.coordinates.y = 845
            self.obstacles.clear()
