import pygame
import time

from classes.player.gun.projectile import Projectile


class Gun:
    CHARGE_SPEED = 3.5
    COOLDOWN_DURATION = 1  # seconds

    def __init__(self):
        self.projectiles = []
        self.charge_modifier = 0
        self.mouse_pressed = False
        self.last_fired_time = 0

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
                self.fire_projectile(player, event)

        if mouse_pressed:
            self.begin_charging()

        self.mouse_pressed = mouse_pressed

    def fire_projectile(self, player, event):
        current_time = time.time()
        if current_time - self.last_fired_time >= self.COOLDOWN_DURATION:
            mouse_pos = event.pos
            direction = self.calculate_projectile_direction(player.camera_pos, mouse_pos)
            self.projectiles.append(Projectile(
                pos=player.map_pos,
                velocity=direction,
                charge_modifier=self.charge_modifier,
                player=player)
            )
            self.charge_modifier = 0
            self.last_fired_time = current_time

    def begin_charging(self):
        self.charge_modifier += self.CHARGE_SPEED
        self.charge_modifier = min(self.charge_modifier, 100)
        print(self.charge_modifier)

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