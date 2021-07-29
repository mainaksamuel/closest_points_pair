#!/usr/bin/env python3

from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index),
    path("points/", views.ClosestPointsDataList.as_view()),
    path("points/<int:pk>/", views.ClosestPointsDataDetails.as_view()),
]
