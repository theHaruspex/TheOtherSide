

class Energy:
    MIN_STAMINA = 1
    MAX_STAMINA = 100
    STAMINA_DEPLETION_RATE = 2
    STAMINA_REPLINISH_RATE = 0.5
    FATIGUE_INCREASE_RATE = 0.5
    FATIGUE_DECREASE_RATE = FATIGUE_INCREASE_RATE / 10
    MAX_FATIGUE = 75

    def __init__(self):
        self.stamina_cap = self.MAX_STAMINA
        self.current_stamina = self.MAX_STAMINA
        self.fatigue_level = 0
        self.is_fatigued = False

    def update(self, gun):
        self.bound_stamina()
        self.handle_gun_charge(gun)
        self.handle_fatigue_value()
        self.handle_fatigue_status(gun)

    def handle_gun_charge(self, gun):
        if gun.is_charging:
            self.current_stamina -= self.STAMINA_DEPLETION_RATE
            # self.fatigue_level += self.FATIGUE_INCREASE_RATE
        elif not gun.is_charged:
            self.current_stamina += self.STAMINA_REPLINISH_RATE
            # self.fatigue_level -= self.FATIGUE_DECREASE_RATE

    def bound_stamina(self):
        self.current_stamina = min(max(self.MIN_STAMINA, self.current_stamina), self.stamina_cap)

    def handle_fatigue_value(self):
        self.fatigue_level = min(max(0, self.fatigue_level), self.MAX_FATIGUE)
        self.stamina_cap = self.MAX_STAMINA - self.fatigue_level
        if not self.is_fatigued:
            self.fatigue_level -= self.FATIGUE_DECREASE_RATE

    def handle_fatigue_status(self, gun):
        if self.current_stamina > self.stamina_cap * 0.7:
            self.is_fatigued = False
        elif self.current_stamina <= self.MIN_STAMINA:
            self.is_fatigued = True
            gun.charge_modifier = gun.MIN_CHARGE
