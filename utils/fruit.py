from .settings import *
import random


class Fruit:
    def __init__(self):
        self.colors = [RED, GREEN, BLUE]
        self.color = random.choice(self.colors)
        self.size = PIXEL_SIZE
        self.position = random.randint(0, 29) * 20, random.randint(0, 24) * 20
        self.body = pygame.Rect(*self.position, self.size, self.size)

    def generate_new_fruit_pos(self, snake):
        x, y = random.randint(0, 29) * 20, random.randint(0, 24) * 20
        for part in snake.body:
            if part.x == x and part.y == y:
                x, y = self.generate_new_fruit_pos(snake)
        return x, y

    def generate_new_fruit(self, snake):  # checar se fruta esta dentro da cobra
        self.position = self.generate_new_fruit_pos(snake)
        self.color = random.choice(self.colors)
        self.body = pygame.Rect(*self.position, self.size, self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.body)
