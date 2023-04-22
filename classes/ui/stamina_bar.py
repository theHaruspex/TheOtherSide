import pygame


class StaminaBar:
    # Constants
    HEIGHT = 10
    BASE_COLOR = (0, 0, 0)
    STAMINA_COLOR = (0, 255, 0)
    FATIGUE_COLOR = (255, 0, 0)

    def __init__(self, screen_dimensions):
        screen_width, screen_height = screen_dimensions

        # Initialize properties of the stamina bar
        self.full_width = screen_width // 3
        self.current_width = self.full_width

        # Calculate the position and width of the bars
        x = (screen_width - self.full_width) // 2
        y = screen_height - self.HEIGHT * 2

        # Create the base surface of the stamina bar
        self.base_rect = pygame.Rect(x, y, self.full_width, self.HEIGHT)
        self.base_image = pygame.Surface((self.full_width, self.HEIGHT)).convert()
        self.base_image.fill(self.BASE_COLOR)

        # Create the stamina surface of the stamina bar
        self.stamina_rect = pygame.Rect(x, y, self.full_width, self.HEIGHT)
        self.stamina_image = pygame.Surface((self.full_width, self.HEIGHT)).convert()
        self.front_color = self.STAMINA_COLOR
        self.stamina_image.fill(self.front_color)

    def update_stamina(self, stamina):
        # Convert stamina (valued at a range from 0 to 100) into bar width
        bar_width = (stamina / 100) * self.full_width

        # Ensure that the new width is within the bounds of the bar
        self.current_width = max(0, bar_width)
        self.current_width = min(bar_width, self.full_width)


        if stamina > 0:
            # Create a new stamina surface with the updated width
            self.stamina_image = pygame.Surface((self.current_width, self.HEIGHT))
            self.stamina_image.fill(self.front_color)
            self.stamina_rect.width = self.current_width

    def update_fatigue(self, player_is_fatigued):
        if player_is_fatigued:
            self.front_color = self.FATIGUE_COLOR
        else:
            self.front_color = self.STAMINA_COLOR


    def draw(self, surface):
        surface.blit(self.base_image, self.base_rect)
        surface.blit(self.stamina_image, self.stamina_rect)

    def update(self, player, surface):
        self.update_fatigue(player.energy.is_fatigued)
        self.update_stamina(player.energy.current_stamina)
        self.draw(surface)

