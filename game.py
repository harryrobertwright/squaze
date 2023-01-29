from dataclasses import dataclass
from dataclasses import field

from constants import Direction
from models import Score
from objects import Obstacle
from objects import Player
from screen import Screen


@dataclass
class Game:
    obstacles: list[Obstacle] = field(default_factory=list)
    player: Player = Player()
    screen: Screen = Screen()
    round: int = 0
    bombs: int = 0

    @property
    def difficulty(self):
        return self.round * 10

    def move_player(self, direction: Direction) -> None:
        x, y = direction.value
        self.player.move(x, y)

        if self.player.check_collision(self.obstacles):
            self.player.move(-x, -y)

    def spawn_obstacles(self) -> None:
        obstacles = Obstacle.create_batch(self.difficulty)
        self.obstacles.extend(obstacles)

    def destroy_obstacles(self) -> None:
        if not self.bombs:
            return

        if self.player.index is not None:
            self.obstacles.pop(self.player.index)
            self.bombs -= 1
            self.player.index = None

    def new_round(self) -> None:
        if not self.obstacles:
            score = Score({"value": self.round})
            score.save()
            self.round += 1
            self.bombs += 1
            self.spawn_obstacles()

        if self.player.rect.y == 0:
            self.player.rect.x = 0
            self.player.rect.y = 865
            self.obstacles.clear()
