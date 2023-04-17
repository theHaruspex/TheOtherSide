import pygame


class Player:
    PLAYER_COLOR = (255, 255, 255)  # white
    WIDTH = 50
    HEIGHT = 50
    ABSOLUTE_MAX_STAMINA = 100
    BASE_SPEED = 10
    SPRINT_SPEED = BASE_SPEED * 2
    STAMINA_DEPLETION_RATE = 1
    STAMINA_REPLINISH_RATE = 0.5
    THIRST_INCREASE_RATE = 0.1

    def __init__(self, x, y):
        # Create a surface for the player and fill it with white color
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.fill(self.PLAYER_COLOR)

        # Get the rectangle that contains the player's image and set its position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Define the player's initial stamina, movement parameters, and thirst level
        self.max_stamina = self.ABSOLUTE_MAX_STAMINA
        self.current_stamina = self.ABSOLUTE_MAX_STAMINA
        self.current_speed = self.BASE_SPEED
        self.sprint_cooldown = False
        self.is_moving = False
        self.thirst_level = 0

    def bound_stamina(self):
        self.current_stamina = min(self.current_stamina, self.max_stamina)
        self.current_stamina = max(0, self.current_stamina)

    def is_sprinting(self) -> bool:
        keys = pygame.key.get_pressed()
        return keys[pygame.K_SPACE] and not self.sprint_cooldown and self.is_moving

    def handle_sprint_cooldown(self):
        if self.current_stamina > self.max_stamina * 0.7:
            self.sprint_cooldown = False

        if self.current_stamina <= 0:
            self.sprint_cooldown = True
            self.current_speed = self.BASE_SPEED

    def handle_sprint(self):
        # If the player is sprinting, set the speed to sprint speed, deplete stamina, and increase thirst
        if self.is_sprinting():
            self.current_speed = self.SPRINT_SPEED
            self.current_stamina -= self.STAMINA_DEPLETION_RATE
            if self.thirst_level < 75:
                self.thirst_level += self.THIRST_INCREASE_RATE

        # If the player is not sprinting, restore the player's speed and stamina
        else:
            self.current_speed = self.BASE_SPEED
            self.current_stamina += self.STAMINA_REPLINISH_RATE

        # Check if the player's sprint cooldown needs to be triggered or reset, and bound the stamina
        self.handle_sprint_cooldown()
        self.bound_stamina()

    def handle_thirst(self):
        # Bound thirst to a number between 0 and 75
        self.thirst_level = max(0, self.thirst_level)
        self.thirst_level = min(self.thirst_level, 75)
        self.max_stamina = self.ABSOLUTE_MAX_STAMINA - self.thirst_level

    def handle_keys(self):
        moving = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.current_speed, 0)
            moving = True
        elif keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.current_speed, 0)
            moving = True
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -self.current_speed)
            moving = True
        elif keys[pygame.K_DOWN]:
            self.rect.move_ip(0, self.current_speed)
            moving = True
        self.is_moving = moving

    def keep_within_bounds(self, map_surface):
        map_rect = pygame.Rect(0, 0, map_surface.get_width(), map_surface.get_height())
        self.rect.clamp_ip(map_rect)

    def handle_movement(self, map_surface):
        self.handle_thirst()
        self.handle_sprint()
        self.handle_keys()
        self.keep_within_bounds(map_surface)

    def draw(self, screen, camera):
        screen.blit(
            self.image,
            self.rect.move(-camera.rect.x, -camera.rect.y)
        )

    def update(self, map_surface, screen, camera):
        self.handle_movement(map_surface)
        self.draw(screen, camera)
