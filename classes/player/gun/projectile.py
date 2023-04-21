import pygame
import math


class Projectile:
    COLOR = (255, 255, 255)
    SIZE = 10
    SPEED = 20

    def __init__(self, pos, velocity):
        self.x, self.y = pos
        self.velocity_x, self.velocity_y = velocity

        # Calculate the length of the velocity vector
        velocity_length = math.sqrt(self.velocity_x ** 2 + self.velocity_y ** 2)

        # Normalize the velocity vector
        if velocity_length > 0:
            self.velocity_x /= velocity_length
            self.velocity_y /= velocity_length

        # Scale the velocity vector
        self.velocity_x *= self.SPEED
        self.velocity_y *= self.SPEED

    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def draw(self, map_surface):
        pygame.draw.rect(map_surface, self.COLOR, (self.x, self.y, self.SIZE, self.SIZE))
