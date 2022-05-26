from .settings import *

class Grid:
    def __init__(self):
        self.rows = (WIDTH  - GAME_BAR_HEIGHT) // PIXEL_SIZE
        self.cols = HEIGHT // PIXEL_SIZE
        self.color = BLACK
    
    def draw(self, screen):
        for row in range(self.rows + 1):
            pygame.draw.line(screen, self.color, (0, row * PIXEL_SIZE), (WIDTH + PIXEL_SIZE, row * PIXEL_SIZE))
        for col in range(self.cols + 1):
            pygame.draw.line(screen, self.color, (col * PIXEL_SIZE, 0), (col * PIXEL_SIZE, HEIGHT - GAME_BAR_HEIGHT))
    
