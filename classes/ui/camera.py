import pygame


class Camera:
    def __init__(self, screen_dimensions):
        screen_width, screen_height = screen_dimensions
        self.rect = pygame.Rect(0, 0, screen_width, screen_height)

    def update(self, player, background_surface, background_image):
        background_surface.blit(background_image, (0, 0))
        self.rect.center = player.rect.center
        self.rect.clamp_ip(background_surface.get_rect())
