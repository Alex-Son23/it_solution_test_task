from django.shortcuts import render
from rest_framework import generics, filters, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Car
from .serializers import CarSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CarsFilter
from .pagination import CustomPagination


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarsFilter
    ordering = [
        "id",
    ]
    ordering_fields = ["mileage", "price"]
    pagination_class = CustomPagination
    # filter_backends = []
    filtering_fields = []
    # permission_classes = (IsAuthenticated,)
