import time


class CalculateDuration:
    def __init__(self):
        self.duration = None
        self._start_time = None
        self._end_time = None
        self.start()

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    
    def start(self):
        self._start_time = time.time()

    def stop(self):
        self._end_time = time.time()

    def calculate(self):
        if self._end_time is None or self._end_time < self._start_time:
            self._end_time = time.time()
        self.duration = self._end_time - self._start_time
        return self.duration


# Exemple d'utilisation de la classe
if __name__ == "__main__":
    duration = CalculateDuration()
    print(f"start_time: {duration.start_time}")
    # Pause de 2 secondes pour démonstration
    time.sleep(2)
    # Calcul de la durée
    duration.calculate()
    print(f"Durée: {duration.duration}")
    # Modifier start_time via le setter
    duration.start_time = time.time()
    print(f"start_time: {duration.start_time}")
    time.sleep(1)
    # Recalcul de la durée avec le nouveau start_time
    duration.calculate()
    print(f"Durée: {duration.duration}")
