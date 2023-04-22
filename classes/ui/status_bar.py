import pygame


class StatusBar:
    # Constants
    WIDTH = 10
    BASE_COLOR = (0, 0, 0)
    TOP_COLOR = (255, 255, 255)
    TEXT_COLOR = (255, 255, 255)
    FONT_SIZE = 24

    def __init__(self, screen_dimensions, status_name=""):
        screen_width, screen_height = screen_dimensions
        # Initialize properties of the top bar
        self.full_height = screen_height // 3
        self.current_height = 0  # Start at the bottom

        # Calculate the position and width of the bars
        x = screen_width - (self.WIDTH * 2)
        y = (screen_height // 2) + (self.full_height // 2)

        # Create the base and top surfaces and rectangles
        self.init_rectangles(x, y)
        self.init_surfaces()

        self.name = status_name

        # Create the font object for the text
        self.font = pygame.font.SysFont(None, self.FONT_SIZE)


    def init_rectangles(self, x, y):
        self.base_rect = pygame.Rect(x, y - self.full_height, self.WIDTH, self.full_height)
        self.front_rect = pygame.Rect(x, y, self.WIDTH, self.current_height)

    def init_surfaces(self):
        self.base_image = pygame.Surface((self.WIDTH, self.full_height)).convert()
        self.base_image.fill(self.BASE_COLOR)

        self.front_image = pygame.Surface((self.WIDTH, self.current_height)).convert()
        self.front_image.fill(self.TOP_COLOR)

    def update_status(self, status_value):
        # Convert top (valued at a range from 0 to 100) into bar height
        self.current_height = (status_value / 100) * self.full_height

        # Update the position and size of the front bar rectangle
        self.front_rect.height = self.current_height
        self.front_rect.y = self.base_rect.y + self.full_height - self.current_height

        # Create a new top surface with the updated height
        self.front_image = pygame.Surface((self.WIDTH, self.current_height))
        self.front_image.fill(self.TOP_COLOR)

    def get_display_text_pos(self):
        name_text = self.font.render(self.name, True, self.TEXT_COLOR)
        name_text_width = name_text.get_width()
        text_x = self.base_rect.x - name_text_width - self.WIDTH
        text_y = self.base_rect.y + self.base_rect.height // 2 - name_text.get_height() // 2
        return text_x, text_y

    def draw(self, surface):
        surface.blit(self.base_image, self.base_rect)
        if self.front_image.get_height() > 0:
            surface.blit(self.front_image, self.front_rect)

        # Render the name of the status to the left of the bar
        # display_text_pos = self.get_display_text_pos()
        # surface.blit(self.font.render(self.name, True, self.TEXT_COLOR), display_text_pos)

    def update(self, status_value, surface):
        self.update_status(status_value)
        self.draw(surface)
