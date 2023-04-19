class Stamina:
    ABSOLUTE_MAX_STAMINA = 100
    STAMINA_DEPLETION_RATE = 1
    STAMINA_REPLENISH_RATE = 0.5

    MAX_FATIGUE = 75
    FATIGUE_INCREASE_RATE = 0.3
    FATIGUE_DECREASE_RATE = FATIGUE_INCREASE_RATE / 4



    def __init__(self):
        self.max_stamina = self.ABSOLUTE_MAX_STAMINA
        self.current_stamina = self.ABSOLUTE_MAX_STAMINA
        self.fatigue_buildup = 0
        self.is_fatigued = False


    def handle_stamina(self):
        print(f"1: {self.current_stamina}")

        self.current_stamina += self.STAMINA_REPLENISH_RATE

        self.current_stamina = min(self.current_stamina, self.max_stamina)
        self.current_stamina = max(0, self.current_stamina)
        print(f"2: {self.current_stamina}")
        print()

    def handle_fatigue(self, player):
        if self.current_stamina > self.max_stamina * 0.7:
            self.is_fatigued = False

        if self.current_stamina <= 0:
            self.is_fatigued = True

        if self.is_fatigued:
            if player.velocity_x > player.max_velocity:
                player.velocity_x = player.max_velocity
            elif player.velocity_x < -player.max_velocity:
                player.velocity_x = -player.max_velocity
            if player.velocity_y > player.max_velocity:
                player.velocity_y = player.max_velocity
            elif player.velocity_y < -player.max_velocity:
                player.velocity_y = -player.max_velocity

    def handle_thirst(self):
        self.fatigue_buildup = max(0, self.fatigue_buildup)
        self.fatigue_buildup = min(self.fatigue_buildup, self.MAX_FATIGUE)
        self.max_stamina = self.ABSOLUTE_MAX_STAMINA - self.fatigue_buildup
        if not self.is_fatigued:
            self.fatigue_buildup -= self.FATIGUE_DECREASE_RATE

    def handle_sprint_logic(self, player):
        if not player.is_moving or self.is_fatigued:
            player.stop_sprinting()

        else:
            player.stop_sprinting()

    def update(self, player):
        self.handle_thirst()
        self.handle_fatigue(player)
        self.handle_sprint_logic(player)
        self.handle_stamina()

    def handle_sprinting(self):
        self.current_stamina -= self.STAMINA_DEPLETION_RATE
        if self.fatigue_buildup < self.MAX_FATIGUE:
            self.fatigue_buildup += self.FATIGUE_INCREASE_RATE
