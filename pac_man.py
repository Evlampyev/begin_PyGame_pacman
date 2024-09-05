import pygame
import time

pac_man_color = (255, 255, 0)


class Pac_man(object):

    def __init__(self, width, height):
        self.screen_width = width
        self.screen_height = height
        self.radius = 20
        self.step = 8
        self.x = width // 2 - self.radius // 2
        self.y = height // 2 - self.radius // 2
        self.face = "open"
        self.image = '1.png'

    def draw(self, surface):
        """Отрисовка пакмана"""
        surface.blit(pygame.image.load(self.image), (self.x, self.y))

    def update(self, x_change, y_change):
        """Обновление положения пакмана"""
        self.x += x_change
        self.y += y_change
        if self.x < 1:
            self.x = 1
        if self.y < 1:
            self.y = 1
        if self.x > self.screen_width - self.radius * 2:
            self.x = self.screen_width - self.radius * 2
        if self.y > self.screen_height - self.radius * 2:
            self.y = self.screen_height - self.radius * 2

    def change_face(self):
        """Изменение внешнего вида пакмана"""
        if self.face == "open":
            self.face = "close"
            self.image = '2.png'
        else:
            self.face = "open"
            self.image = '1.png'

    def eat_enemy(self, enemy_x, enemy_y, radius):
        """Проверка попадания пакмана на врага"""
        if abs((self.x + self.radius) - (enemy_x + radius)) <= (self.radius + radius-3) and abs(
                (self.y + self.radius) - (enemy_y + radius)) <= (self.radius + radius-3):
            return False
        else:
            return True
