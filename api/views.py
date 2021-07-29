from typing import Dict
from django.http import Http404

from backend.utils import parse_request, get_closest_pair
from backend.models import ClosestPointsData

from .serializers import ClosestPointsDataSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


def calculate_closest_points(data: Dict) -> Dict:
    submitted = data.get("submitted_points")
    if submitted:
        parsed = parse_request(submitted)
        point1, point2 = get_closest_pair(parsed)
        closest_pair = f"{point1}, {point2}"
        return {"submitted_points": submitted, "closest_pair": closest_pair}
    else:
        return data


class ClosestPointsDataList(APIView):
    def get(self, request, format=None):
        closest_points = ClosestPointsData.objects.all()
        serializer = ClosestPointsDataSerializer(closest_points, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        data = calculate_closest_points(request.data)
        serializer = ClosestPointsDataSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClosestPointsDataDetails(APIView):
    def get_data(self, pk):
        try:
            return ClosestPointsData.objects.get(pk=pk)
        except ClosestPointsData.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        points_data = self.get_data(pk)
        serializer = ClosestPointsDataSerializer(points_data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        points_data = self.get_data(pk)
        data = calculate_closest_points(request.data)
        serializer = ClosestPointsDataSerializer(points_data, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        points_data = self.get_data(pk)
        points_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
