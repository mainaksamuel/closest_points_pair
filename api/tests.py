from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.

from backend.utils import parse_request, get_closest_pair
from backend.models import Point, ClosestPointsData


class ApiTests(TestCase):
    def test_single_point_from_single_point_input(self):
        string_input = "(2,3)"
        parsed_points = parse_request(string_input)
        closest_pair = get_closest_pair(parsed_points)
        expected = [Point(2, 3)]

        self.assertEqual(len(closest_pair), len(expected))
        first_calculated = f"{ closest_pair[0] }"
        first_expected = f"{expected[0]}"
        self.assertEqual(first_calculated, first_expected)

    def test_ignores_non_points_input(self):
        string_input = "(2 this is invalid input"
        parsed_points = parse_request(string_input)
        closest_pair = get_closest_pair(parsed_points)
        expected = []
        self.assertEqual(len(closest_pair), len(expected))


class ApiRestTests(APITestCase):
    def test_creation_of_closest_points_pair_data(self):
        url = reverse("points")
        data = {"submitted_points": "(2,3), (1,1), (5,4)"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ClosestPointsData.objects.count(), 1)
        self.assertEqual(
            ClosestPointsData.objects.get().submitted_points, "(2,3), (1,1), (5,4)"
        )
        self.assertEqual(ClosestPointsData.objects.get().closest_pair, "(2, 3), (1, 1)")

    def test_retrieve_single_closest_points_pair_data(self):
        create_url = reverse("points")
        data = {"submitted_points": "(2,3), (1,1), (5,4)"}
        create_response = self.client.post(create_url, data, format="json")
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        retrieve_url = reverse("points-details", args=[1])
        retrieve_response = self.client.get(retrieve_url, format="json")
        self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)
        self.assertEqual(ClosestPointsData.objects.count(), 1)
        self.assertEqual(
            ClosestPointsData.objects.get().submitted_points,
            retrieve_response.data["submitted_points"],
        )
        self.assertEqual(
            ClosestPointsData.objects.get().closest_pair,
            retrieve_response.data["closest_pair"],
        )

    def test_update_closest_points_pair_data(self):
        create_url = reverse("points")
        data = {"submitted_points": "(2,3), (1,1), (5,4)"}
        create_response = self.client.post(create_url, data, format="json")
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        details_url = reverse("points-details", args=[1])
        retrieve_response = self.client.get(details_url, format="json")
        self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)

        update_data = {"submitted_points": "(22,33), (11,11), (55,44)"}
        update_response = self.client.put(details_url, update_data, format="json")
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)

        self.assertEqual(ClosestPointsData.objects.count(), 1)
        self.assertEqual(
            ClosestPointsData.objects.get().submitted_points,
            update_data["submitted_points"],
        )

    def test_delete_single_closest_points_pair_data(self):
        create_url = reverse("points")
        data = {"submitted_points": "(2,3), (1,1), (5,4)"}
        create_response = self.client.post(create_url, data, format="json")
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        details_url = reverse("points-details", args=[1])
        retrieve_response = self.client.get(details_url, format="json")
        self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)

        delete_response = self.client.delete(details_url)
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(ClosestPointsData.objects.count(), 0)

    def test_returns_404_for_closest_points_pair_data_notfound(self):
        url = reverse("points-details", args=[1])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_returns_status_400_for_non_point_input(self):
        url = reverse("points")
        data = {"submitted_points": "no points submitted"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
