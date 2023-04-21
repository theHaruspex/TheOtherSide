import pygame
import time

from classes.player.gun.projectile import Projectile


class Gun:
    CHARGE_SPEED = 3.5
    MAX_CHARGE = 100
    MIN_CHARGE = 1
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
        left_pressed, _, right_pressed = pygame.mouse.get_pressed()
        self.handle_charging(right_pressed, player)
        self.shoot_projectile(player) if left_pressed else None

    def reset_charge(self):
        self.charge_modifier = self.MIN_CHARGE
        self.is_charging = False
        self.is_charged = False

    def handle_charging(self, right_pressed, player):
        if not right_pressed:
            self.reset_charge()
            return

        if player.energy.is_fatigued:
            self.is_charging = False
            return

        self.charge_modifier = min(self.charge_modifier + self.CHARGE_SPEED, self.MAX_CHARGE)
        self.is_charging = self.charge_modifier < self.MAX_CHARGE
        self.is_charged = self.charge_modifier == self.MAX_CHARGE

    def shoot_projectile(self, player):
        if player.energy.is_fatigued:
            return

        current_time = time.time()
        if current_time - self.last_shot_time >= self.COOLDOWN_DURATION:
            mouse_pos = pygame.mouse.get_pos()
            self.projectiles.append(
                Projectile(
                    pos=player.map_pos,
                    direction=self.calculate_projectile_direction(player.camera_pos, mouse_pos),
                    charge_modifier=self.charge_modifier,
                    player=player
                )
            )
            self.last_shot_time = current_time
            self.reset_charge()

    def update_projectiles(self, map_surface):
        [projectile.update(map_surface) for projectile in self.projectiles]

    def update(self, player, map_surface):
        self.handle_mouse(player)
        self.update_projectiles(map_surface)
