import pygame
from pac_man import Pac_man
from enemy import Enemy
from time import time

screen_width = 800
screen_height = 800
end_time = 100
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
fps = 60


def create_enemy_list():
    enemy_list = []
    for i in range(4):
        enemy_list.append(Enemy(screen_width, screen_height))
    return enemy_list


class Game(object):
    def __init__(self):
        self.fon = BLUE
        self.screen = None
        self.running = True
        self.init_pygame()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 30)
        self.time_begin = time()
        self.time = 0
        self.point = 0

    def init_pygame(self):
        """Инициализация Pygame"""
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Pac-man")
        self.pac_man = Pac_man(screen_width, screen_height)
        self.enemy_list = create_enemy_list()

    def run(self):
        """Главный цикл игры"""
        x = y = time()
        while self.running:
            self.event_handling()
            self.update()
            self.draw()
            self.clock.tick(fps)

            if time() - x > 0.3:
                self.pac_man.change_face()
                x = time()
            for enemy in self.enemy_list:
                enemy.update()

            if time() - y > 5:
                y = time()
                for enemy in self.enemy_list:
                    enemy.change_direction()

        self.quit_game()

    def event_handling(self):
        """Обработка событий"""
        x_change = 0
        y_change = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        x_change = 0
        y_change = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x_change = -self.pac_man.step
        elif keys[pygame.K_RIGHT]:
            x_change = self.pac_man.step
        elif keys[pygame.K_UP]:
            y_change = -self.pac_man.step
        elif keys[pygame.K_DOWN]:
            y_change = self.pac_man.step

        self.pac_man.update(x_change, y_change)

    def update(self):
        """Обновление состояния"""
        self.screen.fill(self.fon)
        self.pac_man.draw(self.screen)
        for enemy in self.enemy_list:
            if enemy.visible:
                enemy.visible = self.pac_man.eat_enemy(enemy.x, enemy.y, enemy.radius)
                if not enemy.visible:
                    self.point += 1
            enemy.draw(self.screen)

        self.time = int(time() - self.time_begin)
        time_surface = self.font.render(f"Время: {str(self.time)} сек", True, WHITE)
        point_surface = self.font.render(f"Очки: {str(self.point)}", True, WHITE)
        if self.time >= end_time:
            self.running = False
        self.screen.blit(time_surface, (0, 0))
        self.screen.blit(point_surface, (screen_width - point_surface.get_width(), 0))

        pygame.display.update()

    def draw(self):
        """Отрисовка элементов на экране."""
        pygame.display.flip()
        next_enemy_list = False
        for enemy in self.enemy_list:
            next_enemy_list += enemy.visible
        if not next_enemy_list:
            self.enemy_list = create_enemy_list()

    def quit_game(self):
        """Окончание игры"""
        game_over_surface = pygame.font.SysFont("Arial", 30).render("Игра окончена", True, WHITE)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (screen_width // 2, screen_height // 4)
        self.screen.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        pygame.time.wait(5000)


if __name__ == "__main__":
    game = Game()
    game.run()
