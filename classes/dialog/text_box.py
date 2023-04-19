import pygame


class TextBox:
    FADE_OUT_RATE = 5
    MAX_ALPHA = 255
    MAIN_COLOR = (255, 255, 255)
    ALT_COLOR = (255, 0, 0)

    def __init__(self, x, y, init_text, font_size=25, wrap_width=500, is_clickable=False):
        self.x = x
        self.y = y

        self.width = None
        self.height = None
        self.wrap_width = wrap_width

        self.font_size = font_size
        self.font_color = self.MAIN_COLOR
        self.font = pygame.font.Font(None, self.font_size)

        self.text = init_text
        self.text_lines = []
        self.current_line = ''
        self.line_height = 1.5 * self.font.size('Tg')[1]  # test line height
        self.add_text(init_text)

        self.update_dimensions()

        self.alpha = 0
        self.is_fading_in = True

        self.is_clickable = is_clickable
        self.is_mouse_over = self.detect_mouse_over()

    def render(self, surface):
        self.blit_text_lines(surface)
        self.update_dimensions()
        self.handle_mouse_over()

        if self.is_fading_in:
            self.fade_in()

    def blit_text_lines(self, surface):
        y = self.y
        for line in self.text_lines:
            rendered_text = self.font.render(line, True, self.font_color)
            rendered_text.set_alpha(self.alpha)
            surface.blit(rendered_text, (self.x, y))
            y += self.line_height

    def update_dimensions(self):
        self.width = max([self.font.size(line)[0] for line in self.text_lines])
        self.height = len(self.text_lines) * self.line_height

    def add_text(self, text):
        self.current_line = ''
        words = text.split()
        for word in words:
            test_line = self.current_line + word + ' '
            if self.font.size(test_line)[0] < self.wrap_width:
                self.current_line = test_line
            else:
                self.text_lines.append(self.current_line)
                self.current_line = word + ' '
        self.text_lines.append(self.current_line)

    def fade_in(self):
        self.alpha += self.FADE_OUT_RATE
        if self.alpha > self.MAX_ALPHA:
            self.alpha = 255
            self.is_fading_in = False

    def detect_mouse_over(self):
        mouse_pos = pygame.mouse.get_pos()
        return (self.x <= mouse_pos[0] <= self.x + self.width and
                self.y <= mouse_pos[1] <= self.y + self.height)

    def change_color(self):
        if self.font_color == self.MAIN_COLOR:
            self.font_color = self.ALT_COLOR
        else:
            self.font_color = self.MAIN_COLOR

    def handle_mouse_over(self):
        is_mouse_over = self.detect_mouse_over()
        if self.is_clickable:
            if is_mouse_over != self.is_mouse_over:
                self.is_mouse_over = is_mouse_over
                self.change_color()

    def detect_click(self):
        mouse_click = pygame.mouse.get_pressed()[0]
        if mouse_click and self.detect_mouse_over() and not self.is_fading_in:
            return True
        else:
            return False
