import django_filters
from .models import Car


class CarsFilter(django_filters.rest_framework.FilterSet):
    brand = django_filters.CharFilter(lookup_expr="icontains")
    model = django_filters.CharFilter(lookup_expr="icontains")
    year = django_filters.NumberFilter()
    fuel_type = django_filters.CharFilter(lookup_expr="icontains")
    transmission = django_filters.CharFilter(lookup_expr="icontains")
    price = django_filters.RangeFilter()
    mileage = django_filters.RangeFilter()

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
