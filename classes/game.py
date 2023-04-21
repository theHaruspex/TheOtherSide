import pygame

from classes.ui.user_interface import UserInterface
from classes.player.player import Player
from classes.ui.camera import Camera


class Game:
    MAP_IMG = pygame.image.load('resources/backdrop.png')
    MAP_IMG = pygame.transform.scale(MAP_IMG, (5000, 5000))
    MAP_SURFACE = pygame.Surface((MAP_IMG.get_width(), MAP_IMG.get_height()))

    def __init__(self, screen_dimensions):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_dimensions, pygame.FULLSCREEN)
        self.ui = UserInterface(screen_dimensions)
        self.player = Player(1000, 1000)
        self.camera = Camera(screen_dimensions)

    def update(self):
        self.screen.blit(self.MAP_SURFACE, (0, 0), self.camera)
        self.camera.update(self.player, self.MAP_SURFACE, self.MAP_IMG)
        self.player.update(self.MAP_SURFACE, self.screen, self.camera)
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
