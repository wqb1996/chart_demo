from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path("",views.),
]
route = DefaultRouter()
route.register("chartdata", views.ChartDBViewSet)
urlpatterns += route.urls
