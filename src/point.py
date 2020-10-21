"""Plik zawierający klasę punktu siatki i obliczeń na nim"""


class point:
    """Klasa punktu siatki"""

    # Stałe dla wszystkich punktów - póki co tutaj
    lambda_val = 380  # Wartość lambdy
    density_val = 9000  # Gęstość
    specific_heat_val = 380  # Ciepło właściwe

    def __init__(self, value: float):
        """Inicjalizacja punktu"""

        self.backward_value = None  # Wartość temperatury w poprzednim punkcie
        self.value = value  # Wartość temperatury w punkcie
        self.forward_value = None  # Wartość temperatury w następnym punkcie

    def __str__(self):
        return ("Temperatue at point %.2lf" %self.value)

    def calculate(self, time_delta: float, distance_delta: float) -> None:
        """Wykonaj obliczenia dla punktu"""

        self.value += time_delta * self.lambda_val / \
            (distance_delta ** 2) / self.density_val / self.specific_heat_val * \
            (self.backward_value - 2 * self.value + self.forward_value)

