import pygame

from classes.ui.user_interface import UserInterface
from classes.ui.camera import Camera

from classes.player.player import Player

from classes.map.map import Map


class Game:
    def __init__(self, screen_dimensions):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_dimensions, pygame.FULLSCREEN)
        self.ui = UserInterface(screen_dimensions)
        self.player = Player(1000, 1000)
        self.camera = Camera(screen_dimensions)
        self.current_map = Map()

    def update(self):
        self.current_map.update(self.screen, self.camera)
        self.camera.update(self.player, self.current_map.surface, self.current_map.image)
        self.player.update(self.current_map.surface, self.screen, self.camera)
        self.ui.update(self.screen, self.player)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.update()
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
