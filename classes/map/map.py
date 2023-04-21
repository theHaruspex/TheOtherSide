import pygame


class Map:

    def __init__(self, image_filepath='resources/backdrop.png', size=5000):
        image = pygame.image.load(image_filepath)

        # Assumes map image is square
        self.image = pygame.transform.scale(image, (size, size))
        self.surface = pygame.Surface((size, size))

    def update(self, screen, camera):
        screen.blit(self.surface, (0, 0), camera)