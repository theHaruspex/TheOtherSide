import pygame

from classes.dialog.text_box import TextBox
from classes.dialog.dialogue_tree import DialogueTree

from classes.dialog.sample_values import *


class Scene:
    TITLE_X = 440
    TITLE_Y = 50
    TITLE_FONT_SIZE = 70

    NPC_TEXT_X = 440
    NPC_TEXT_Y = 180

    PORTRAIT_X = 40
    PORTRAIT_Y = 50
    PORTRAIT_SIZE = (335, 500)

    BACKGROUND_OVERLAY_COLOR = (0, 0, 0)
    BACKGROUND_OVERLAY_ALPHA = 200

    def __init__(self):
        self.dialogue_tree = DialogueTree(prophetess_dialogue)

        self.title = self.create_title_box()
        self.npc_dialogue = None
        self.options = None
        self.update_dialogue()

        self.portrait = pygame.image.load(sample_portrait_path).convert()
        self.portrait = pygame.transform.scale(self.portrait, self.PORTRAIT_SIZE)
        self.background = pygame.image.load(sample_background_path).convert()

    def create_title_box(self):
        return TextBox(
            x=self.TITLE_X,
            y=self.TITLE_Y,
            init_text="The Prophetess",
            font_size=self.TITLE_FONT_SIZE
        )

    def draw_options(self, surface):
        for option in self.options:
            option.render(surface)

    def update_dialogue(self):
        self.npc_dialogue = TextBox(
            x=self.NPC_TEXT_X,
            y=self.NPC_TEXT_Y,
            init_text=self.dialogue_tree.get_current_node_text()
        )

        self.options = [
            TextBox(x=500, y=400 + i * 50, init_text=option_text, is_clickable=True)
            for i, option_text in enumerate(self.dialogue_tree.get_current_node_options())
        ]

    def handle_option_select(self):
        for option in self.options:
            if option.handle_click():
                selected_option = option.text
                self.dialogue_tree.select_option(selected_option)
                self.update_dialogue()

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
        self.handle_option_select()
        self.npc_dialogue.render(screen)
        self.draw_portrait(screen)
        self.draw_options(screen)
        pygame.display.update()
