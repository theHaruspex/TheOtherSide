import pygame
import math


class Projectile:
    COLOR = (255, 255, 255)
    BASE_SIZE = 10
    BASE_SPEED = 10

    def __init__(self, pos, velocity, charge_modifier):
        self.x, self.y = pos
        self.velocity_x, self.velocity_y = velocity
        self.size = self._scale_size(charge_modifier)
        self.speed = self._scale_speed(charge_modifier)
        self._scale_velocity()

    def _scale_size(self, charge_modifier):
        size_modifier = charge_modifier / 100
        return int(self.BASE_SIZE * (1 + size_modifier))

    def _scale_speed(self, charge_modifier):
        speed_modifier = 1 + (2 * charge_modifier / 100)
        return int(self.BASE_SPEED * speed_modifier)

    def _scale_velocity(self):
        # Calculate the length of the velocity vector
        velocity_length = math.sqrt(self.velocity_x ** 2 + self.velocity_y ** 2)

        # Normalize the velocity vector
        if velocity_length > 0:
            self.velocity_x /= velocity_length
            self.velocity_y /= velocity_length

        # Scale the velocity vector
        self.velocity_x *= self.speed
        self.velocity_y *= self.speed

    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def draw(self, map_surface):
        pygame.draw.rect(map_surface, self.COLOR, (self.x, self.y, self.size, self.size))
