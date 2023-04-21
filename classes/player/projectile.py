import pygame


class Projectile:
    PROJECTILE_COLOR = (255, 0, 0)
    PROJECTILE_RADIUS = 3
    PROJECTILE_SPEED = 10

    def __init__(self, start_pos, end_pos):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.rect = pygame.Rect(start_pos[0], start_pos[1], 0, 0)
        self.alive = True
        self.speed = pygame.math.Vector2(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]).normalize() * self.PROJECTILE_SPEED

    def update(self, map_surface):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        if not map_surface.get_rect().colliderect(self.rect):
            self.alive = False


    def render(self, screen, camera):
        pygame.draw.circle(screen, self.PROJECTILE_COLOR, (int(self.rect.centerx - camera.rect.x), int(self.rect.centery - camera.rect.y)), self.PROJECTILE_RADIUS)

