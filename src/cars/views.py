from django.http import Http404
from rest_framework import viewsets, status
from .models import Car
from .serializers import CarSerializer
from .filters import CarsFilter
from .pagination import CustomPagination
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    retrieve=extend_schema(
        summary="Получение заявки на создание торговой сети.",
        # parameters=[join_request_param],
    ),
    partial_update=extend_schema(
        summary="Изменение заявки на создание торговой сети.",
        # parameters=[join_request_param],
    ),
    list=extend_schema(summary="Получение списка заявок на создание торговой сети."),
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
