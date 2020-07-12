from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .serializer import ChartInfoSerializer
from .models import ChartInfo


class ChartDBViewSet(ModelViewSet):
    serializer_class = ChartInfoSerializer
    queryset = ChartInfo.objects.all()
