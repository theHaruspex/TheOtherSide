import pygame

from classes.player.gun.projectile import Projectile


class Gun:
    def __init__(self):
        self.projectiles = []

    def handle_events(self, player):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                # Add a new projectile to the list based on the mouse position
                mouse_x, mouse_y = event.pos
                player_x, player_y = player.camera_pos

                dx = mouse_x - player_x
                dy = mouse_y - player_y

                self.projectiles.append(Projectile(player.map_pos, (dx, dy)))

    def update_projectiles(self):
        for projectile in self.projectiles:
            projectile.update()

    def draw(self, map_surface):
        for projectile in self.projectiles:
            projectile.draw(map_surface)

    def update(self, player, map_surface):
        self.handle_events(player)
        self.update_projectiles()
        self.draw(map_surface)
