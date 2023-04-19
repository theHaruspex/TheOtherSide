from classes.ui.stamina_bar import StaminaBar
from classes.ui.status_bar import StatusBar


class UserInterface:
    def __init__(self, screen_dimensions):
        self.stamina_bar = StaminaBar(screen_dimensions)
        self.health_bar = StatusBar(screen_dimensions, 1, "Health")

    def update(self, screen, player):
        # Update the stamina bar
        self.stamina_bar.update(player.stamina.stamina_level, player.stamina.fatigue_level, screen)

        # Update other status bars
        self.health_bar.update(player.health, screen)
