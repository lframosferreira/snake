from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
from .settings import *
from .fruit import Fruit


class Snake:
    def __init__(self, x, y):
        self.color = WHITE
        self.size = PIXEL_SIZE
        self.x = x
        self.y = y
        self.body = [pygame.Rect(self.x, self.y, self.size, self.size)]
        self.velocity_x = 0
        self.velocity_y = 0
        self.fruits_eaten = 0
        self.record = current_record

    def draw(self, screen):
        for part in self.body:
            pygame.draw.rect(screen, self.color, part)

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.velocity_x
        self.body[0].y += self.velocity_y
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_UP] and not self.velocity_y:  # up
            self.velocity_x = 0
            self.velocity_y = -1 * SNAKE_VELOCITY
        if keys_pressed[K_DOWN] and not self.velocity_y:  # down
            self.velocity_x = 0
            self.velocity_y = SNAKE_VELOCITY
        if keys_pressed[K_RIGHT] and not self.velocity_x:  # right
            self.velocity_x = SNAKE_VELOCITY
            self.velocity_y = 0
        if keys_pressed[K_LEFT] and not self.velocity_x:  # left
            self.velocity_x = -1 * SNAKE_VELOCITY
            self.velocity_y = 0

    def update_record(self, file="utils/record.txt"):
        if self.fruits_eaten > self.record:
            self.record = self.fruits_eaten
        with open(file, "w") as file:
            file.write(str(self.record))

    def eat_fruit(self, fruit):
        if self.body[0].colliderect(fruit.body):
            self.fruits_eaten += 1
            new_part = pygame.Rect(
                self.body[len(self.body) - 1].x,
                self.body[len(self.body) - 1].y,
                self.size,
                self.size,
            )
            self.body.append(new_part)
            fruit.generate_new_fruit(self)
        self.update_record()

    def restart(self):
        self.fruits_eaten = 0
        self.body.clear()
        self.body.append(pygame.Rect(self.x, self.y, self.size, self.size))
