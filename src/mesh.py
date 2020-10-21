"""Plik zawierający klasę generujacą siatkę i wykonującą na niej operacje"""

from typing import List

from point import point


class mesh:

    def __init__(self, size: float, element_num: int, tempL: float, tempR: float):
        self.size = size
        self.element_num = element_num
        self.points = []
        self.distance_delta = size / element_num

        # Uzupełnij punkty od lewej do prawej
        for i in range(0, element_num):
            if i < element_num / 2:
                self.points.append(point(tempL))
            else:
                self.points.append(point(tempR))

        # Od razu zaktualizuj by wypełnić pola przed i za puktów
        self.update_mesh()

    def __repr__(self):
        for point in self.points:
            print ("%.0f" % point.value)
        return "Jestem siatką"
        

    def update_mesh(self):
        """Przepisz dane punktów do sąsiednich punktów"""

        # Pierwszy punkt jako wartość przed ma swoją wartość
        self.points[0].backward_value = self.points[0].value
        self.points[1].backward_value = self.points[0].value

        # Środkowe punkty przepisują do sąsiednich
        for i in range(1, len(self.points) - 1):
            self.points[i-1].forward_value = self.points[i].value
            self.points[i+1].backward_value = self.points[i].value

        # Ostatni punkt jako wartość za ma swoją wartość
        self.points[-1].forward_value = self.points[-1].value
        self.points[-2].forward_value = self.points[-1].value

    def step_mesh(self, time_delta: float):
        """Dokonaj obliczenia dla punktów siatki"""

        # TU TRZEBA RÓWNOLEGLIĆ
        for point in self.points:
            point.calculate(time_delta, self.distance_delta)
