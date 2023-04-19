import pygame

from classes.player.stamina import Stamina
from classes.player.movement import Movement


class Player:
    # Image
    PLAYER_COLOR = (255, 255, 255)
    WIDTH = 50
    HEIGHT = 50

    # Stats
    MAX_HEALTH = 100

    def __init__(self, x, y):
        # Image
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.fill(self.PLAYER_COLOR)

        # Positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Movement
        self.movement = Movement()

        # Stats
        self.stamina = Stamina()
        self.health = self.MAX_HEALTH

    # Executive functions
    def update(self, map_surface, screen, camera):
        self.handle_mouse()
        self.movement.update(self, map_surface)
        self.stamina.update()
        self.handle_health()
        self.draw(screen, camera)

    def handle_mouse(self):
        left_click, middle_click, right_click = pygame.mouse.get_pressed()

        if left_click:
            click_pos = pygame.mouse.get_pos()

    def draw(self, screen, camera):
        screen.blit(self.image, self.rect.move(-camera.rect.x, -camera.rect.y))

    # Stats
    def handle_health(self):
        self.health = min(self.health, self.MAX_HEALTH)
        self.health = max(0, self.health)
