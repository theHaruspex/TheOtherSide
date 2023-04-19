import pygame

class Movement:
    BASE_VELOCITY = 15
    FATIGUE_VELOCITY = BASE_VELOCITY // 5
    FRICTION = 0.97

    def __init__(self):
        self.velocity_x = 0
        self.velocity_y = 0
        self.max_velocity = self.BASE_VELOCITY
        self.acceleration = 1
        self.is_moving = False

    def update(self, player, map_surface):
        self.handle_keys()
        self.handle_velocity(player)
        self.handle_object_collision(map_surface, player)

    def handle_velocity(self, player):
        self.velocity_x *= self.FRICTION
        self.velocity_y *= self.FRICTION
        player.rect.move_ip(self.velocity_x, self.velocity_y)
        if player.stamina.is_fatigued:
            self.cap_velocity()

    def handle_object_collision(self, surface, player):
        if player.rect.left <= 0 or player.rect.right >= surface.get_width():
            self.velocity_x = -self.velocity_x
        if player.rect.top <= 0 or player.rect.bottom >= surface.get_height():
            self.velocity_y = -self.velocity_y

    def cap_velocity(self):
        if self.velocity_x > self.FATIGUE_VELOCITY:
            self.velocity_x = self.FATIGUE_VELOCITY
        elif self.velocity_x < -self.FATIGUE_VELOCITY:
            self.velocity_x = -self.FATIGUE_VELOCITY
        if self.velocity_y > self.FATIGUE_VELOCITY:
            self.velocity_y = self.FATIGUE_VELOCITY
        elif self.velocity_y < -self.FATIGUE_VELOCITY:
            self.velocity_y = -self.FATIGUE_VELOCITY

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        moving = False
        if keys[pygame.K_a]:
            self.velocity_x -= self.acceleration
            moving = True
        elif keys[pygame.K_d]:
            self.velocity_x += self.acceleration
            moving = True
        if keys[pygame.K_w]:
            self.velocity_y -= self.acceleration
            moving = True
        elif keys[pygame.K_s]:
            self.velocity_y += self.acceleration
            moving = True
        self.is_moving = moving