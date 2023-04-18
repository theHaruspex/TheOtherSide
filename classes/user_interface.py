import pygame
from classes.player import Player
from classes.stamina_bar import StaminaBar
from classes.camera import Camera
from classes.status_bar import StatusBar
import os

MONITOR_WIDTH = 1024
MONITOR_HEIGHT = 600
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{-MONITOR_WIDTH},{0}"


class UserInterface:
    SCREEN_DIMENSIONS = (MONITOR_WIDTH, MONITOR_HEIGHT)
    BLUE = (42, 46, 92)
    MAP_IMG = pygame.image.load('resources/backdrop.png')
    MAP_IMG = pygame.transform.scale(MAP_IMG, (3000, 3000))
    MAP_SURFACE = pygame.Surface((MAP_IMG.get_width(), MAP_IMG.get_height()))

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.SCREEN_DIMENSIONS, pygame.FULLSCREEN)
        self.player = Player(1000, 1000)
        self.stamina_bar = StaminaBar(self.SCREEN_DIMENSIONS)
        self.health_bar = StatusBar(self.SCREEN_DIMENSIONS, 1, "Health")
        self.hunger_bar = StatusBar(self.SCREEN_DIMENSIONS, 2, "Hunger")
        self.camera = Camera(self.SCREEN_DIMENSIONS)

    def update(self):

        # Draw the background
        self.screen.blit(self.MAP_SURFACE, (0, 0), self.camera)

        # Draw the current player state
        self.player.update(self.MAP_SURFACE, self.screen, self.camera)

        # Update the camera to follow the player
        self.camera.update(self.player, self.MAP_SURFACE, self.MAP_IMG)

        # Update the stamina bar
        self.stamina_bar.update(self.player.current_stamina, self.player.thirst_level, self.screen)

        # Update other status bars
        self.health_bar.update(self.player.health, self.screen)
        self.hunger_bar.update(self.player.hunger, self.screen)

        # Update the screen
        pygame.display.update()
