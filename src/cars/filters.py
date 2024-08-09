import django_filters
from .models import Car


class CarsFilter(django_filters.rest_framework.FilterSet):
    """Фильтр для модели Cars"""

    brand = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Бренд автомобиля",
    )
    model = django_filters.CharFilter(
        lookup_expr="icontains", label="Модель автомобиля"
    )
    year = django_filters.NumberFilter(label="Год выпуска автомобиля")
    fuel_type = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Тип топлива: бензин, дизель, электричество, гибрид",
    )
    transmission = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Тип КПП: механическая, автоматическая, вариатор, робот",
    )
    price = django_filters.RangeFilter(label="Цена")
    mileage = django_filters.RangeFilter(label="Пробег")

    class Meta:
        model = Car
        fields = [
            "brand",
            "model",
            "year",
            "fuel_type",
            "transmission",
            "price",
            "mileage",
        ]
