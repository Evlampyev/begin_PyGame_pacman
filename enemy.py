import pygame
from random import randint

directions = ["up", "down", "left", "right"]


class Enemy(object):

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = randint(0, self.screen_width)
        self.y = randint(0, self.screen_height)
        self.radius = 16
        self.visible = True
        self.direction = directions[randint(0, 3)]
        self.image = pygame.image.load('en_1.png')
        self.step = 5
        self.image = pygame.transform.scale(self.image, (self.radius * 1.5, self.radius * 1.5))

    def draw(self, surface):
        """Отрисовка врага на экране."""
        if self.visible:
            surface.blit(self.image, (self.x, self.y))

    def update(self):
        """Обновление местоположения врага."""
        if self.direction == "up":
            self.y -= self.step
        elif self.direction == "down":
            self.y += self.step
        elif self.direction == "left":
            self.x -= self.step
        elif self.direction == "right":
            self.x += self.step

        if self.x < 0:
            self.x = 0
            self.direction = "right"
        if self.y < 0:
            self.y = 0
            self.direction = "down"
        if self.x > self.screen_width - self.radius * 2:
            self.x = self.screen_width - self.radius * 2
            self.direction = "left"
        if self.y > self.screen_height - self.radius * 2:
            self.y = self.screen_height - self.radius * 2
            self.direction = "up"

    def change_direction(self):
        """Изменение направления движения врага."""
        self.direction = directions[randint(0, 3)]
