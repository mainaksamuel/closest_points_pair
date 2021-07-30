#!/usr/bin/env python3

import re
import sys
import math
import ast
from typing import Any, List

from .models import Points, Point


def parse_request(text: str) -> Points:
    """Parse a string input into a list of Points"""
    pattern = r"\([-+]?[0-9]*\.?[0-9]+\s*,{1}\s*[-+]?[0-9]*\.?[0-9]+\)"
    matches = re.findall(pattern, text)

    points_list = Points()

    for point in matches:
        pattern = r"[-+]?[0-9]*\.?[0-9]+"
        matches = re.findall(pattern, point)
        x, y = ast.literal_eval(matches[0]), ast.literal_eval(matches[1])
        points_list.add_point(Point(x, y))

    return points_list


def get_closest_pair(points: Points) -> List[Point]:
    """
    Calculate the closest points pair from a list of point.
    (Euclidean Space)
    """
    shortest_distance = sys.maxsize

    if points.get_count() < 2:
        return points.get_points()

    closest_pair = [Any] * 2

    for i in range(points.get_count() - 1):
        for j in range(i + 1, points.get_count()):
            x1, x2 = points[i].x, points[j].x
            y1, y2 = points[i].y, points[j].y

            distance = math.hypot(x1 - x2, y1 - y2)

            if distance < shortest_distance:
                shortest_distance = distance
                closest_pair[0] = points[i]
                closest_pair[1] = points[j]

    return closest_pair
