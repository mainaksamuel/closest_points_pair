from typing import List
from django.db import models

# Create your models here.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Points:
    def __init__(self):
        self._points: List[Point] = []

    def get_points(self) -> List[Point]:
        return self._points

    def get_count(self) -> int:
        return len(self._points)

    def add_point(self, point: Point):
        self._points.append(point)

    def __getitem__(self, index) -> Point:
        return self._points[index]

    def __str__(self) -> str:
        # TODO : represent Points without the `__str__()` method
        return ", ".join([point.__str__() for point in self._points])


class ClosestPoints(models.Model):
    submitted_points = models.TextField()
    closest_pair = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.submitted_points}\n {self.closest_pair}"
