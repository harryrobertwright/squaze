from screen import Screen
from objects import *
import random
from dataclasses import dataclass, field


@dataclass
class Game:
    obstacles: list = field(default_factory=list)
    player: Player = Player()
    round: int = 0
    screen: Screen = Screen()

    def collide_check(self, test_rect):
        tolerance = 1

        return any(
            test_rect.colliderect(tuple(obstacle.rect[i] - tolerance for i in range(4)))
            for obstacle in self.obstacles
        )

    def boundary_check(self, test_rect):
        return 0 <= test_rect[0] < (
            self.screen.width - test_rect[2]
        ) and 0 <= test_rect[1] < (self.screen.height - test_rect[3])

    def round_completed(self):
        return self.player.y_pos - self.player.height <= 0

    def update_player_pos(self, x_pos=0, y_pos=0):
        test_rect = pygame.Rect(
            self.player.x_pos + x_pos,
            self.player.y_pos + y_pos,
            self.player.width,
            self.player.height,
        )
        if not self.collide_check(test_rect) and self.boundary_check(test_rect):
            self.player.x_pos += x_pos
            self.player.y_pos += y_pos
            self.player.rect = test_rect

    def spawn_obstacles(self):
        rects = []
        for _ in range(self.get_difficulty()):
            obstacle = Obstacle()
            if obstacle.rect.collidelist(rects) == -1:
                self.obstacles.append(obstacle)
                rects.append(obstacle.rect)

    def get_difficulty(self):
        return self.round * 10

    def new_round(self):
        if not self.obstacles:
            self.round += 1
            self.spawn_obstacles()

        if self.round_completed() == True:
            self.player.x_pos = 0
            self.player.y_pos = 845
            self.obstacles.clear()
