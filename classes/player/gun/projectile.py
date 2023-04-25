import pygame
import math

from classes.sound import Sound

class Projectile:
    COLOR = (255, 255, 255)
    BASE_SIZE = 10
    BASE_SPEED = 3

    def __init__(self, pos, direction, charge_modifier, player):
        self.x, self.y = pos
        self.direction_x, self.direction_y = direction
        self.velocity_x, self.velocity_y = None, None
        self.size = self._scale_size(charge_modifier)
        self.speed = self._scale_speed(charge_modifier)
        self._scale_velocity(player)
        self.knock_back_player(player)
        Sound.play_sound('pew')


    def _scale_size(self, charge_modifier):
        size_modifier = charge_modifier / 100
        return int(self.BASE_SIZE * (1 + size_modifier))

    def _scale_speed(self, charge_modifier):
        speed_modifier = 1 + (2 * charge_modifier / 100)
        return int(self.BASE_SPEED * speed_modifier)

    def knock_back_player(self, player):
        player.movement.velocity_x -= self.velocity_x
        player.movement.velocity_y -= self.velocity_y

    def _scale_velocity(self, player):
        # Calculate and normalize the velocity vector
        velocity_length = math.hypot(self.direction_x, self.direction_y)
        self.velocity_x, self.velocity_y = (
        self.direction_x / velocity_length, self.direction_y / velocity_length) if velocity_length > 0 else (0, 0)

        # Scale the velocity vector
        self.velocity_x *= self.speed
        self.velocity_y *= self.speed

        # Calculate the dot product of the projectile's velocity and the player's velocity
        dot_product = self.velocity_x * player.movement.velocity_x + self.velocity_y * player.movement.velocity_y

        # Steal or subtract the player's velocity based on the dot product
        if dot_product > 0:
            self.velocity_x += player.movement.velocity_x
            self.velocity_y += player.movement.velocity_y
        elif dot_product < 0:
            player.movement.velocity_x -= self.velocity_x
            player.movement.velocity_y -= self.velocity_y

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def draw(self, map_surface):
        pygame.draw.rect(map_surface, self.COLOR, (self.x, self.y, self.size, self.size))

    def update(self, map_surface):
        self.move()
        self.draw(map_surface)
