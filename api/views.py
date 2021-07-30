from typing import Dict
from django.http import Http404

from backend.utils import parse_request, get_closest_pair
from backend.models import ClosestPointsData

from .serializers import ClosestPointsDataSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.


@api_view(["GET"])
def api_index(request):
    """API paths descriptions"""
    api_urls = {
        "List Closest Points Pair Data": {"url_path": "/api/points/", "method": "GET"},
        "Detail view of a record": {
            "url_path": "/api/points/<int:id>/",
            "method": "GET",
        },
        "Create a record": {"url_path": "/api/points/", "method": "POST"},
        "Update a record": {"url_path": "/api/points/<int:id>/", "method": "PUT"},
        "Delete a record": {"url_path": "/api/points/<int:id>/", "method": " DELETE"},
        "API Documentation": {
            "url_path": "/api/points/schema/swagger-ui/",
            "method": " GET",
        },
    }

    return Response(api_urls)


def calculate_closest_points(data: Dict) -> Dict:
    """Returns the closest points pair, otherwise the parameter itself"""
    submitted = data.get("submitted_points")
    if submitted:
        parsed = parse_request(submitted.strip())
        pair = get_closest_pair(parsed)

        if len(pair) == 2:
            point1, point2 = pair
            closest_pair = f"{point1}, {point2}"
            return {"submitted_points": submitted, "closest_pair": closest_pair}
        elif len(pair) == 1:
            closest_pair = f"{pair[0]}"
            return {"submitted_points": submitted, "closest_pair": closest_pair}
        else:
            return dict()

    else:
        return data


class ClosestPointsDataList(APIView):
    serializer_class = ClosestPointsDataSerializer

    def get(self, request, format=None):
        """Get all the Closest Points Pair Data"""
        closest_points = ClosestPointsData.objects.all()
        serializer = ClosestPointsDataSerializer(closest_points, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Post a string of Points to get the closest points pair
        Only the `submitted_points` field is required for input
        """
        pair_points = calculate_closest_points(request.data)
        serializer = ClosestPointsDataSerializer(data=pair_points)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClosestPointsDataDetails(APIView):
    serializer_class = ClosestPointsDataSerializer

    def get_data(self, pk):
        try:
            return ClosestPointsData.objects.get(pk=pk)
        except ClosestPointsData.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """Get a single Closest Points Pair Data record from the primary key"""
        points_data = self.get_data(pk)
        serializer = ClosestPointsDataSerializer(points_data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Update a Closest Points Pair Data record using the primary key
        Only the `submitted_points` field is required for input
        """
        points_data = self.get_data(pk)
        data = calculate_closest_points(request.data)
        serializer = ClosestPointsDataSerializer(points_data, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """Delete a Closest Points Pair Data record using the primary key"""
        points_data = self.get_data(pk)
        points_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
