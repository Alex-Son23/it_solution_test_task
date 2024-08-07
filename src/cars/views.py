from django.shortcuts import render
from rest_framework import generics, filters, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Car
from .serializers import CarSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CarsFilter
from .pagination import CustomPagination
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarsFilter
    ordering = [
        "id",
    ]
    ordering_fields = ["mileage", "price"]
    pagination_class = CustomPagination
    # permission_classes = (IsAuthenticated,)

    # @swagger_auto_schema(
    #     manual_parameters=[
    #         openapi.Parameter(
    #             "price_min",
    #             openapi.IN_QUERY,
    #             description="Minimum price",
    #             type=openapi.TYPE_NUMBER,
    #         ),
    #         openapi.Parameter(
    #             "price_max",
    #             openapi.IN_QUERY,
    #             description="Maximum price",
    #             type=openapi.TYPE_NUMBER,
    #         ),
    #         openapi.Parameter(
    #             "mileage_min",
    #             openapi.IN_QUERY,
    #             description="Minimum mileage",
    #             type=openapi.TYPE_INTEGER,
    #         ),
    #         openapi.Parameter(
    #             "mileage_max",
    #             openapi.IN_QUERY,
    #             description="Maximum mileage",
    #             type=openapi.TYPE_INTEGER,
    #         ),
    #     ]
    # )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
