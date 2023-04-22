from classes.ui.stamina_bar import StaminaBar
from classes.ui.status_bar import StatusBar


class UserInterface:
    def __init__(self, screen_dimensions):
        self.stamina_bar = StaminaBar(screen_dimensions)
        self.charge_bar = StatusBar(screen_dimensions)

    def update(self, screen, player):
        # Update the stamina bar
        self.stamina_bar.update(player, screen)

        # Update other status bars
        self.charge_bar.update(player.gun.charge_modifier, screen)
