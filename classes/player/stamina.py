

class Stamina:
    MAX_STAMINA = 100
    STAMINA_DEPLETION_RATE = 1
    STAMINA_REPLINISH_RATE = 0.5
    FATIGUE_INCREASE_RATE = 0.3
    FATIGUE_DECREASE_RATE = FATIGUE_INCREASE_RATE / 4
    MAX_FATIGUE = 75

    def __init__(self):
        self.stamina_cap = self.MAX_STAMINA
        self.stamina_level = self.MAX_STAMINA
        self.fatigue_level = 0
        self.is_fatigued = False

    def update(self):
        self.stamina_level -= 1
        self.bound_stamina()
        self.handle_fatigue_value()
        self.handle_fatigue_status()

    def bound_stamina(self):
        self.stamina_level = min(self.stamina_level, self.stamina_cap)
        self.stamina_level = max(0, self.stamina_level)

    def handle_fatigue_value(self):
        self.fatigue_level = max(0, self.fatigue_level)
        self.fatigue_level = min(self.fatigue_level, 75)
        self.stamina_cap = self.MAX_STAMINA - self.fatigue_level
        if not self.is_fatigued:
            self.fatigue_level -= self.FATIGUE_DECREASE_RATE

    def handle_fatigue_status(self):
        if self.stamina_level > self.stamina_cap * 0.7:
            self.is_fatigued = False

        if self.stamina_level <= 0:
            self.is_fatigued = True
