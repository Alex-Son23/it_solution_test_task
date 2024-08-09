from django.http import Http404
from rest_framework import viewsets, status
from .models import Car
from .serializers import CarSerializer
from .filters import CarsFilter
from .pagination import CustomPagination
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter


@extend_schema_view(
    retrieve=extend_schema(
        summary="Получения данных о машине.",
    ),
    partial_update=extend_schema(
        summary="Изменения данных о машине.",
    ),
    list=extend_schema(
        summary="Получение списка машин.",
        description="Возвращает список машин с возможностью фильтрации по цене (минимальная и максимальная) и другим параметрам.",
        parameters=[
            OpenApiParameter(
                name="price_min",
                description="Минимальная цена",
                required=False,
                type=int,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name="price_max",
                description="Максимальная цена",
                required=False,
                type=int,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name="mileage_min",
                description="Минимальный пробег",
                required=False,
                type=int,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name="mileage_max",
                description="Максимальный пробег",
                required=False,
                type=int,
                location=OpenApiParameter.QUERY,
            ),
            # Добавьте другие параметры по необходимости
        ],
    ),
    create=extend_schema(
        summary="Создание новой машины.",
    ),
    update=extend_schema(
        summary="Полное обновление данных о машине.",
    ),
    destroy=extend_schema(
        summary="Удаление машины.",
    ),
)
class CarViewSet(viewsets.ModelViewSet):
    """View для модели Car"""

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarsFilter
    ordering = [
        "id",
    ]
    ordering_fields = ["mileage", "price"]
    pagination_class = CustomPagination

    def retrieve(self, request, *args, **kwargs):
        try:
            car = self.get_object()
        except Http404:
            raise NotFound(
                detail="Автомобиль с данным ID не найден",
                code=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.get_serializer(car)
        return Response(serializer.data)
