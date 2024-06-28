import time


class CalculateDuration:
    def __init__(self):
        self.duration = None
        self._start_time = time.time()
        print(f"Start time: {self._start_time:.6f}")
        self._end_time = None

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
        print(f"Start time updated to {value:.6f}")

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
        print(f"End time updated to {value:.6f}")

    def calculate(self):
        if self._end_time is None or self._end_time < self._start_time:
            self.end_time = time.time()
        self.duration = self._end_time - self._start_time
        print(f"Duration elapsed: {self.duration:.6f} second(s)")
        return self.duration


# Exemple d'utilisation de la classe
if __name__ == "__main__":
    duration = CalculateDuration()
    # Pause de 2 secondes pour démonstration
    time.sleep(2)
    # Calcul de la durée
    duration.calculate()
    # Modifier start_time via le setter
    duration.start_time = time.time()
    time.sleep(1)
    # Recalcul de la durée avec le nouveau start_time
    duration.calculate()
