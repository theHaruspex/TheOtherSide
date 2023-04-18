import pygame


import pygame

class StatusBar:
    # Constants
    HEIGHT = 10
    BASE_COLOR = (0, 0, 0)
    TOP_COLOR = (255, 255, 255)
    TEXT_COLOR = (255, 255, 255)
    FONT_SIZE = 24

    def __init__(self, screen_dimensions, stack_order, status_name):
        screen_width, screen_height = screen_dimensions
        # Initialize properties of the top bar
        self.full_width = screen_width // 5
        self.current_width = self.full_width

        # Calculate the position and width of the bars
        x = (screen_width // 20)
        y = stack_order * 100

        # Create the base surface of the top bar
        self.base_rect = pygame.Rect(x, y, self.full_width, self.HEIGHT)
        self.base_image = pygame.Surface((self.full_width, self.HEIGHT)).convert()
        self.base_image.fill(self.BASE_COLOR)

        # Create the top surface of the top bar
        self.top_rect = pygame.Rect(x, y, self.full_width, self.HEIGHT)
        self.top_image = pygame.Surface((self.full_width, self.HEIGHT)).convert()
        self.top_image.fill(self.TOP_COLOR)

        self.name = status_name

        # Create the font object for the text
        self.font = pygame.font.SysFont(None, self.FONT_SIZE)

    def update_status(self, status_value):
        # Convert top (valued at a range from 0 to 100) into bar width
        bar_width = (status_value / 100) * self.full_width

        # Ensure that the new width is within the bounds of the bar
        self.current_width = max(0, bar_width)
        self.current_width = min(bar_width, self.full_width)

        # Create a new top surface with the updated width
        self.top_image = pygame.Surface((self.current_width, self.HEIGHT))
        self.top_image.fill(self.TOP_COLOR)
        self.top_rect.width = self.current_width

    def draw(self, surface):
        surface.blit(self.base_image, self.base_rect)
        surface.blit(self.top_image, self.top_rect)

        # Render the name of the status on the bar
        name_text = self.font.render(self.name, True, self.TEXT_COLOR)
        name_text_height = name_text.get_height()
        text_x = self.base_rect.x
        text_y = self.base_rect.y - self.HEIGHT - name_text_height
        surface.blit(name_text, (text_x, text_y))

    def update(self, player_status, surface):
        self.update_status(player_status)
        self.draw(surface)
