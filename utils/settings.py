import pygame

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 600, 600
GAME_BAR_WIDHT, GAME_BAR_HEIGHT = WIDTH, 100

# colors
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
GREY = 64, 64, 64

FPS = 15

PIXEL_SIZE = 20

SNAKE_VELOCITY = PIXEL_SIZE

with open("utils/record.txt", "r") as file:
    current_record = int(file.read())
