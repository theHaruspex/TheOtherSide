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

        # Create the base and top surfaces and rectangles
        self.init_rectangles(x, y)
        self.init_surfaces()

        self.name = status_name

        # Create the font object for the text
        self.font = pygame.font.SysFont(None, self.FONT_SIZE)

    def init_rectangles(self, x, y):
        self.base_rect = pygame.Rect(x, y, self.full_width, self.HEIGHT)
        self.top_rect = pygame.Rect(x, y, self.full_width, self.HEIGHT)

    def init_surfaces(self):
        self.base_image = pygame.Surface((self.full_width, self.HEIGHT)).convert()
        self.base_image.fill(self.BASE_COLOR)

        self.top_image = pygame.Surface((self.full_width, self.HEIGHT)).convert()
        self.top_image.fill(self.TOP_COLOR)

    def update_status(self, status_value):
        # Convert top (valued at a range from 0 to 100) into bar width
        self.current_width = (status_value / 100) * self.full_width

        # Create a new top surface with the updated width
        self.top_image = pygame.Surface((self.current_width, self.HEIGHT))
        self.top_image.fill(self.TOP_COLOR)

        self.top_rect.width = self.current_width

    def get_display_text_pos(self):
        name_text = self.font.render(self.name, True, self.TEXT_COLOR)
        name_text_height = name_text.get_height()
        text_x = self.base_rect.x
        text_y = self.base_rect.y - self.HEIGHT - name_text_height
        return text_x, text_y

    def draw(self, surface):
        surface.blit(self.base_image, self.base_rect)
        surface.blit(self.top_image, self.top_rect)

        # Render the name of the status on the bar
        display_text_pos = self.get_display_text_pos()
        surface.blit(self.font.render(self.name, True, self.TEXT_COLOR), display_text_pos)

    def update(self, player_status, surface):
        self.update_status(player_status)
        self.draw(surface)
