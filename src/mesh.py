"""Plik zawierający klasę generujacą siatkę i wykonującą na niej operacje"""

from typing import List

import pyspark

from point import point
from config import initials


class mesh:

    def __init__(self, size: float, element_num: int):
        self.size = size
        self.element_num = element_num
        self.points = []
        self.distance_delta = size / element_num

        # Uzupełnij punkty od lewej do prawej
        for i in range(0, element_num):
            if i < element_num / 2:
                self.points.append(point(initials.temp_left))
            else:
                self.points.append(point(initials.temp_right))

        # Od razu zaktualizuj by wypełnić pola przed i za puktów
        self.update_mesh()

    def __repr__(self):
        for point in self.points:
            print("%.0f" % point.value)
        return "Jestem siatką"

    def data_return(self):
        data=[]
        for point in self.points:
            data.append(point.value)
        return data

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

    def step_mesh(self, time_delta: float, context: pyspark.SparkContext) -> float:
        """Dokonaj obliczenia dla punktów siatki"""

        local_distance_delta = self.distance_delta
        rdd = context.parallelize(self.points).map(lambda point: point.calculate(time_delta, local_distance_delta))

        # TODO: wydaje mi się, że to rozwiązanie jest dość wolne...
        i = 0
        for point in rdd.collect():
            self.points[i] = point
            i += 1
        
        return abs(self.points[0].value-self.points[i-1].value)