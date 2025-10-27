import pygame
from pygame import Vector2

from game.level import Level
from core.time import Time
from game.player import Player
from game.monster import Monster


screen_width = 600
screen_height = 900


class App:
    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((screen_width, screen_height))
        self._level = Level(Vector2(screen_width, screen_height))
        self._is_running = True
        self._level.entities.append(Player(self._level))
        self._level.entities.append(Monster(self._level))
    
    # TODO: Frame limit. Calculate delta time.
    def run_main_loop(self):
        # Main Loop
        while self._is_running:
            # Basic window event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._is_running = False
                    break
            self.update()
            self.draw()
            Time.tick()
    
    def get_is_running(self) -> bool:
        return self._is_running
    
    def get_level(self) -> Level:
        return self._level

    def update(self):
        self._level.update()

    def draw(self):
        self._screen.fill((0, 0, 0))           # Clear the screen.
        self._level.draw(self._screen)
        pygame.display.update()
    
