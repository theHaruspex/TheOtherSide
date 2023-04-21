import pygame

from classes.player.energy import Energy
from classes.player.movement import Movement
from classes.player.gun.gun import Gun


class Player:
    PLAYER_COLOR = (255, 255, 255)
    WIDTH = 30
    HEIGHT = 30
    MAX_HEALTH = 100

    def __init__(self, x, y):
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.fill(self.PLAYER_COLOR)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.movement = Movement()
        self.energy = Energy()
        self.gun = Gun()

        self.health = self.MAX_HEALTH

        self.camera_pos = self.rect.center
        self.map_pos = None

    def update(self, map_surface, screen, camera):
        # Update the player's position by smaller increments
        self.movement.update(self, map_surface)
        self.rect.move_ip(self.movement.velocity_x, self.movement.velocity_y)

        self.energy.update(self.gun)
        self.gun.update(self, map_surface)
        self.handle_health()
        self.draw(screen, camera)
        self.update_camera_pos(camera)
        self.update_map_position(map_surface)

    def handle_health(self):
        self.health = min(self.health, self.MAX_HEALTH)
        self.health = max(0, self.health)

    def draw(self, screen, camera):
        screen.blit(self.image, self.rect.move(-camera.rect.x, -camera.rect.y))

    def update_camera_pos(self, camera):
        self.camera_pos = (self.rect.centerx - camera.rect.x, self.rect.centery - camera.rect.y)

    def update_map_position(self, map_surface):
        collision_rect = self.rect.clip(map_surface.get_rect())
        if collision_rect.width == 0 or collision_rect.height == 0:
            # no collision
            self.map_pos = None
        else:
            # collision detected
            self.map_pos = collision_rect.center
