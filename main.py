from utils.fonts import SCORE_FONT
from utils import *
import pygame


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")


def draw_screen(screen, snake, fruit, grid):
    score_text = SCORE_FONT.render("Score: " + str(snake.fruits_eaten), 1, WHITE)
    screen.blit(
        score_text,
        (
            WIDTH // 4 - score_text.get_width() // 2,
            HEIGHT - GAME_BAR_HEIGHT // 2 - score_text.get_height() // 2,
        ),
    )
    record_text = SCORE_FONT.render("Record: " + str(snake.record), 1, WHITE)
    screen.blit(
        record_text,
        (
            WIDTH - WIDTH // 4 - record_text.get_width() // 2,
            HEIGHT - GAME_BAR_HEIGHT // 2 - record_text.get_height() // 2,
        ),
    )
    snake.draw(screen)
    fruit.draw(screen)
    grid.draw(screen)


def draw_buttons(screen):
    pass


def draw_lost_text(screen):
    pygame.draw.rect(
        screen,
        WHITE,
        (
            PIXEL_SIZE * 6,
            PIXEL_SIZE * 6,
            HEIGHT - PIXEL_SIZE * 12,
            WIDTH - PIXEL_SIZE * 12,
        ),
    )
    lost_text = LOST_FONT.render("Your score: " + str(snake.fruits_eaten), 1, BLACK)
    screen.blit(
        lost_text,
        (
            WIDTH // 2 - lost_text.get_width() // 2,
            HEIGHT // 2 - lost_text.get_height() // 2,
        ),
    )


def lost_game(snake):
    if snake.body[0].x < 0 or snake.body[0].x + SNAKE_VELOCITY > WIDTH:
        return True
    if (
        snake.body[0].y < 0
        or snake.body[0].y + SNAKE_VELOCITY > HEIGHT - GAME_BAR_HEIGHT
    ):
        return True
    if snake.body[0].collidelist(snake.body[1 : len(snake.body)]) != -1:
        return True
    return False


snake = Snake(100, 100)
fruit = Fruit()
grid = Grid()
restart_button = Button(200, 400, 200, 50, text="Restart")
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if restart_button.clicked(pos):
                snake.restart()

    SCREEN.fill(GREY)
    snake.eat_fruit(fruit)
    snake.move()
    draw_screen(SCREEN, snake, fruit, grid)
    if lost_game(snake):
        snake.velocity_x, snake.velocity_y = 0, 0
        draw_lost_text(SCREEN)
        restart_button.draw(SCREEN)
    pygame.display.update()

pygame.quit()
