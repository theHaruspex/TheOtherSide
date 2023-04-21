import pygame
import math


class Projectile:
    COLOR = (255, 255, 255)
    BASE_SIZE = 10
    BASE_SPEED = 13

    def __init__(self, pos, direction, charge_modifier, player):
        self.x, self.y = pos
        self.direction_x, self.direction_y = direction
        self.velocity_x, self.velocity_y = None, None
        self.size = self._scale_size(charge_modifier)
        self.speed = self._scale_speed(charge_modifier)
        self._scale_velocity(player)
        self.knock_back_player(player)

    def knock_back_player(self, player):
        player.movement.velocity_x -= self.velocity_x
        player.movement.velocity_y -= self.velocity_y

    def _scale_size(self, charge_modifier):
        size_modifier = charge_modifier / 100
        return int(self.BASE_SIZE * (1 + size_modifier))

    def _scale_speed(self, charge_modifier):
        speed_modifier = 1 + (2 * charge_modifier / 100)
        return int(self.BASE_SPEED * speed_modifier)

    def _scale_velocity(self, player):
        # Calculate the length of the velocity vector and normalize it
        velocity_length = math.hypot(self.direction_x, self.direction_y)
        if velocity_length > 0:
            self.velocity_x, self.velocity_y = self.direction_x / velocity_length, self.direction_y / velocity_length

        # Scale the velocity vector
        self.velocity_x *= self.speed
        self.velocity_y *= self.speed

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def draw(self, map_surface):
        pygame.draw.rect(map_surface, self.COLOR, (self.x, self.y, self.size, self.size))

    def update(self, map_surface):
        self.move()
        self.draw(map_surface)
