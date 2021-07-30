from django.test import TestCase

# Create your tests here.

from .models import Point
from .utils import parse_request, get_closest_pair


class BackendTests(TestCase):
    def test_parses_integer_points_correctly(self):
        string_input = "(2,3), (1,1), (5, 4)"
        parsed_points = parse_request(string_input)
        expected = [
            Point(2, 3),
            Point(1, 1),
            Point(5, 4),
        ]
        self.assertEqual(parsed_points.get_count(), len(expected))
        first_parsed = f"{ parsed_points[0] }"
        first_expected = f"{expected[0]}"
        self.assertEqual(first_parsed, first_expected)

        second_parsed = f"{ parsed_points[1] }"
        second_expected = f"{expected[1]}"
        self.assertEqual(second_parsed, second_expected)

    def test_parses_negative_points_correctly(self):
        string_input = "(2,-3), (-5, 4)"
        parsed_points = parse_request(string_input)
        expected = [Point(2, -3), Point(-5, 4)]

        self.assertEqual(parsed_points.get_count(), len(expected))
        first_parsed = f"{ parsed_points[0] }"
        first_expected = f"{expected[0]}"
        self.assertEqual(first_parsed, first_expected)

    def test_parses_floating_points_correctly(self):
        string_input = "(3.142,-32), (-5.7689, 4)"
        parsed_points = parse_request(string_input)
        expected = [Point(3.142, -32), Point(-5.7689, 4)]

        self.assertEqual(parsed_points.get_count(), len(expected))
        first_parsed = f"{ parsed_points[0] }"
        first_expected = f"{expected[0]}"
        self.assertEqual(first_parsed, first_expected)

        second_parsed = f"{ parsed_points[1] }"
        second_expected = f"{expected[1]}"
        self.assertEqual(second_parsed, second_expected)

    def test_returns_correct_closest_points_pair(self):
        string_input = "(2,3), (1,1), (5, 4)"
        parsed_points = parse_request(string_input)
        closest_pair = get_closest_pair(parsed_points)
        expected = [Point(2, 3), Point(1, 1)]

        self.assertEqual(len(closest_pair), len(expected))
        first_calculated = f"{ closest_pair[0] }"
        first_expected = f"{expected[0]}"
        self.assertEqual(first_calculated, first_expected)

        second_calculated = f"{ closest_pair[1] }"
        second_expected = f"{expected[1]}"
        self.assertEqual(second_calculated, second_expected)
