import pygame


class Player:
    # Image
    PLAYER_COLOR = (255, 255, 255)
    WIDTH = 50
    HEIGHT = 50

    # Stats
    MAX_HEALTH = 100

    # Stamina
    MAX_STAMINA = 100
    STAMINA_DEPLETION_RATE = 1
    STAMINA_REPLINISH_RATE = 0.5
    FATIGUE_INCREASE_RATE = 0.3
    FATIGUE_DECREASE_RATE = FATIGUE_INCREASE_RATE / 4
    MAX_FATIGUE = 75

    # Velocity
    BASE_VELOCITY = 15
    FATIGUE_VELOCITY = BASE_VELOCITY // 5
    FRICTION = 0.97

    def __init__(self, x, y):
        # Image
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.fill(self.PLAYER_COLOR)

        # Positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Stats
        self.health = self.MAX_HEALTH

        # Stamina
        self.stamina_cap = self.MAX_STAMINA
        self.current_stamina = self.MAX_STAMINA
        self.fatigue_level = 0

        # Velocity
        self.velocity_x = 0
        self.velocity_y = 0
        self.max_velocity = self.BASE_VELOCITY
        self.acceleration = 1

        # Player states
        self.is_moving = False
        self.is_fatigued = False

    # Executive functions
    def update(self, map_surface, screen, camera):
        self.handle_mouse()
        self.handle_movement(map_surface)
        self.handle_stamina()
        self.handle_health()
        self.draw(screen, camera)

    def handle_mouse(self):
        left_click, middle_click, right_click = pygame.mouse.get_pressed()

        if left_click:
            click_pos = pygame.mouse.get_pos()

    def draw(self, screen, camera):
        screen.blit(self.image, self.rect.move(-camera.rect.x, -camera.rect.y))

    # Movement
    def handle_movement(self, map_surface):
        self.handle_velocity(map_surface)
        self.handle_keys()

    def handle_velocity(self, surface):
        self.velocity_x *= self.FRICTION
        self.velocity_y *= self.FRICTION
        self.handle_object_collision(surface)
        self.rect.move_ip(self.velocity_x, self.velocity_y)
        if self.is_fatigued:
            self.cap_velocity()

    def handle_object_collision(self, surface):
        if self.rect.left <= 0 or self.rect.right >= surface.get_width():
            self.velocity_x = -self.velocity_x
        if self.rect.top <= 0 or self.rect.bottom >= surface.get_height():
            self.velocity_y = -self.velocity_y

    def cap_velocity(self):
        if self.velocity_x > self.max_velocity:
            self.velocity_x = self.max_velocity
        elif self.velocity_x < -self.max_velocity:
            self.velocity_x = -self.max_velocity
        if self.velocity_y > self.max_velocity:
            self.velocity_y = self.max_velocity
        elif self.velocity_y < -self.max_velocity:
            self.velocity_y = -self.max_velocity

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

    # Stamina
    def handle_stamina(self):
        self.bound_stamina()
        self.handle_fatigue_value()
        self.handle_fatigue_status()

    def bound_stamina(self):
        self.current_stamina = min(self.current_stamina, self.stamina_cap)
        self.current_stamina = max(0, self.current_stamina)

    def handle_fatigue_value(self):
        self.fatigue_level = max(0, self.fatigue_level)
        self.fatigue_level = min(self.fatigue_level, 75)
        self.stamina_cap = self.MAX_STAMINA - self.fatigue_level
        if not self.is_fatigued:
            self.fatigue_level -= self.FATIGUE_DECREASE_RATE

    def handle_fatigue_status(self):
        if self.current_stamina > self.stamina_cap * 0.7:
            self.is_fatigued = False

        if self.current_stamina <= 0:
            self.is_fatigued = True

    # Stats
    def handle_health(self):
        self.health = min(self.health, self.MAX_HEALTH)
        self.health = max(0, self.health)
