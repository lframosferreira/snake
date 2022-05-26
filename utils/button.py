from utils.fonts import BUTTON_FONT
from pygame import color
from .settings import *

class Button:
    def __init__(self, x, y, width, height, color = BLACK, text_color = BLACK, text = None):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.color = color
        self.text_color = text_color
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 2)
        if self.text:
            button_text = BUTTON_FONT.render(self.text, 1, self.text_color)
            screen.blit(button_text, (self.x + self.width // 2 - button_text.get_width() // 2,
            self.y + self.height // 2 - button_text.get_height() // 2 ))
    
    def clicked(self, pos):
        x,y = pos
        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y >= self.y and y <= self.y + self.height):
            return False
        return True