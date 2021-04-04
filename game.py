from screen import Screen
from objects import *
import random

class Game:
    def __init__(self):
        self.obstacles = []
        self.player = Player()
        self.round = 0
        self.screen = Screen()

    def collide_check(self, test_rect):
        flag = False
        tolerance = 1
        for obstacle in self.obstacles:
            test_obstacle_rect = (obstacle.rect[0] - tolerance, obstacle.rect[1] - tolerance, obstacle.rect[2] - tolerance, obstacle.rect[3] - tolerance)
            if test_rect.colliderect(test_obstacle_rect) == True:
                flag = True

        return flag

    def boundary_check(self, test_rect):
        flag = True
        if test_rect[0] > (self.screen.WIDTH - test_rect[2]):
            flag = False
        if test_rect[0] < 0:
            flag = False
        if test_rect[1] > (self.screen.HEIGHT - test_rect[3]):
            flag = False
        return flag

    def round_completed(self):
        if self.player.y_pos - self.player.height <= 0:
            return True
        else:
            return False

    def update_player_pos(self, x_pos=0, y_pos=0):
        test_rect = pygame.Rect(self.player.x_pos + x_pos, self.player.y_pos + y_pos, self.player.width, self.player.height)
        if self.collide_check(test_rect) == False:
            if not self.boundary_check(test_rect) == False:
                self.player.x_pos += x_pos
                self.player.y_pos += y_pos
                self.player.rect = test_rect


    def spawn_obstacles(self):
        rects = []
        for x in range(0, self.get_difficulty()):
            obstacle = Obstacle()
            if obstacle.rect.collidelist(rects) == -1:
                self.obstacles.append(obstacle)
                rects.append(obstacle.rect)

    def get_difficulty(self):
        obstacle_number = self.round * 10
        return obstacle_number

    def new_round(self):
        if not self.obstacles:
            self.round += 1
            self.spawn_obstacles()

        if self.round_completed() == True:
            self.player.x_pos = 0
            self.player.y_pos = 845
            self.obstacles.clear()

    # def pulsate(self):
    #     for obstacle in self.obstacles:
    #         obstacle.jitter(10)
    #         # obstacle.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    #         # if random.choice(range(0,10)) == 5:
    #         #     increment = random.randint(-5,5)
    #         #     # LOOP EACH ATTRIBUTE INSTEAD BUNCHING THEM All
    #         #     test_rect = obstacle.rect = pygame.Rect(obstacle.x_pos + increment, obstacle.y_pos + increment, obstacle.width + increment, obstacle.height + increment)
    #         #     if self.collide_check(test_rect) == False:
    #         #         obstacle.rect = test_rect
    #         #         self.player.rect = pygame.Rect(self.player.x_pos, self.player.y_pos, self.player.width, self.player.height)
