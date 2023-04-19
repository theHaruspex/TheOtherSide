import pygame
from classes.dialog.text_box import TextBox

sample_dialogue = (
    "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut "
    "laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation "
    "ullamcorper.")

sample_portrait_path = "resources/the_prophetess.jpg"
sample_background_path = "resources/dialogue_background.jpg"


class Scene:
    TITLE_X = 440
    TITLE_Y = 50
    TITLE_FONT_SIZE = 70

    DIALOG_X = 440
    DIALOG_Y = 180

    PORTRAIT_X = 40
    PORTRAIT_Y = 50
    PORTRAIT_SIZE = (335, 500)

    BACKGROUND_OVERLAY_COLOR = (0, 0, 0)
    BACKGROUND_OVERLAY_ALPHA = 200

    def __init__(self):
        self.title = TextBox(
            x=self.TITLE_X,
            y=self.TITLE_Y,
            init_text="The Prophetess",
            font_size=self.TITLE_FONT_SIZE
        )

        self.dialog = TextBox(
            x=self.DIALOG_X,
            y=self.DIALOG_Y,
            init_text=sample_dialogue
        )

        self.options = TextBox(
            x=500,
            y=400,
            init_text="This is the first option",
            is_clickable=True
        )

        self.portrait = pygame.image.load(sample_portrait_path).convert()
        self.portrait = pygame.transform.scale(self.portrait, self.PORTRAIT_SIZE)
        self.background = pygame.image.load(sample_background_path).convert()

    def draw_portrait(self, screen):
        screen.blit(self.portrait, (self.PORTRAIT_X, self.PORTRAIT_Y))

    def draw_background(self, screen):
        screen.blit(self.background, (0, 0))

        overlay = pygame.Surface((screen.get_width(), screen.get_height()))
        overlay.set_alpha(self.BACKGROUND_OVERLAY_ALPHA)
        overlay.fill(self.BACKGROUND_OVERLAY_COLOR)
        screen.blit(overlay, (0, 0))

    def render(self, screen):
        self.draw_background(screen)
        self.title.render(screen)
        self.dialog.render(screen)
        self.draw_portrait(screen)
        self.options.render(screen)
        pygame.display.update()
