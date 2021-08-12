#!/usr/bin/env python3

from django.urls import path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from . import views

urlpatterns = [
    path("", views.api_index, name="api-index"),
    path("points/", views.ClosestPointsDataList.as_view(), name="points"),
    path(
        "points/<int:pk>/",
        views.ClosestPointsDataDetails.as_view(),
        name="points-details",
    ),
    path("points/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "points/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "points/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
