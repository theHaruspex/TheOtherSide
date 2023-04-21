import pygame

from classes.player.gun.projectile import Projectile


class Gun:
    CHARGE_SPEED = 3.5

    def __init__(self):
        self.projectiles = []
        self.charge_modifier = 0
        self.mouse_pressed = False

    @staticmethod
    def calculate_projectile_direction(player_camera_pos, mouse_pos):
        player_x, player_y = player_camera_pos
        mouse_x, mouse_y = mouse_pos
        dx = mouse_x - player_x
        dy = mouse_y - player_y
        return dx, dy

    def handle_events(self, player):
        mouse_pressed = self.mouse_pressed
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pressed = False
                # Add a new projectile to the list based on the mouse position
                mouse_pos = event.pos
                direction = self. \
                    calculate_projectile_direction(player.camera_pos, mouse_pos)
                self.projectiles.append(Projectile(player.map_pos, direction, self.charge_modifier, player))
                self.charge_modifier = 0

        if mouse_pressed:
            self.charge_modifier += self.CHARGE_SPEED
            self.charge_modifier = min(self.charge_modifier, 100)
            print(self.charge_modifier)

        self.mouse_pressed = mouse_pressed

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
