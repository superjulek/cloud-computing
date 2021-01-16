"""Plik zawierający klasę punktu siatki i obliczeń na nim"""

from config import constants

class point:
    """Klasa punktu siatki"""

    def __init__(self, value: float):
        """Inicjalizacja punktu"""

        self.backward_value = None  # Wartość temperatury w poprzednim punkcie
        self.value = value  # Wartość temperatury w punkcie
        self.forward_value = None  # Wartość temperatury w następnym punkcie

    def __str__(self):
        return ("Temperatue at point %.2lf" %self.value)

    def calculate(self, time_delta: float, distance_delta: float) -> None:
        """Wykonaj obliczenia dla punktu"""

        self.value += time_delta * constants.lambda_val / \
            (distance_delta ** 2) / constants.density_val / constants.specific_heat_val * \
            (self.backward_value - 2 * self.value + self.forward_value)
        # TODO: taki quirk żeby działało map na tym
        return self

