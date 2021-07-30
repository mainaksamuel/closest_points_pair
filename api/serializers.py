from rest_framework import serializers

from backend.models import ClosestPointsData


class ClosestPointsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClosestPointsData
        fields = ("pk", "submitted_points", "closest_pair")
        extra_kwargs = {"closest_points": {"required": False}}
