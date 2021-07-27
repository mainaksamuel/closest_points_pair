from typing import List
from django.db import models

# Create your models here.


class Point(models.Model):
    x = models.DecimalField(decimal_places=2)
    y = models.DecimalField(decimal_places=2)

    def __str__(self):
        return f"({self.x}, {self.y})"


class Points:
    def __init__(self):
        # self.points = []
        self.points: List[Point] = []

    def get_points(self) -> List[Point]:
        return [point for point in self.points]

    def __str__(self) -> str:
        # TODO : represent Points without the `__str__()` method
        return ", ".join([point.__str__() for point in self.points])
