#!/usr/bin/env python3

from django.urls import path
from django.http import HttpResponseRedirect

from . import views

urlpatterns = [
    path("", lambda r: HttpResponseRedirect("/api/points")),
    path("points/", views.ClosestPointsDataList.as_view(), name="points"),
    path("points/<int:pk>/", views.ClosestPointsDataDetails.as_view()),
]
