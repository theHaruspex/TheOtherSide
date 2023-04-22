import pygame
import time

from classes.player.gun.projectile import Projectile


class Gun:
    CHARGE_SPEED = 3.5
    MAX_CHARGE = 100
    MIN_CHARGE = 0

    COOLDOWN_DURATION = 1  # seconds

    def __init__(self):
        self.projectiles = []
        self.charge_modifier = self.MIN_CHARGE
        self.last_shot_time = 0
        self.is_charging = False
        self.is_charged = False

    @staticmethod
    def calculate_projectile_direction(player_camera_pos, mouse_pos):
        player_x, player_y = player_camera_pos
        mouse_x, mouse_y = mouse_pos
        dx, dy = (mouse_x - player_x), (mouse_y - player_y)
        return dx, dy

    def handle_mouse(self, player):
        left_pressed = pygame.mouse.get_pressed()[0]
        self.handle_charging(left_pressed, player)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and left_pressed:
                self.shoot_projectile(player)

    def reset_charge(self):
        self.charge_modifier = self.MIN_CHARGE
        self.is_charging = False
        self.is_charged = False

    def handle_charging(self, charge_button, player):
        if not charge_button:
            self.reset_charge()
            return

        if player.energy.is_fatigued:
            self.is_charging = False
            return

        if not self.cooldown:
            self.charge_modifier = min(self.charge_modifier + self.CHARGE_SPEED, self.MAX_CHARGE)
            self.is_charging = self.charge_modifier < self.MAX_CHARGE
            self.is_charged = self.charge_modifier == self.MAX_CHARGE

    def shoot_projectile(self, player):
        if player.energy.is_fatigued:
            return

        if not self.cooldown:
            mouse_pos = pygame.mouse.get_pos()
            self.projectiles.append(
                Projectile(
                    pos=player.map_pos,
                    direction=self.calculate_projectile_direction(player.camera_pos, mouse_pos),
                    charge_modifier=self.charge_modifier,
                    player=player
                )
            )
            self.last_shot_time = time.time()
            self.reset_charge()

    def update_projectiles(self, map_surface):
        [projectile.update(map_surface) for projectile in self.projectiles]

    def update(self, player, map_surface):
        self.handle_mouse(player)
        self.update_projectiles(map_surface)

    @property
    def cooldown(self):
        current_time = time.time()
        return current_time - self.last_shot_time < self.COOLDOWN_DURATION
