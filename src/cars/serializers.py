from rest_framework import serializers
from .models import Car
from datetime import datetime
from django.utils.translation import gettext_lazy as _

CURRENT_YEAR = datetime.now().year


class CarSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Car"""

    brand = serializers.CharField(max_length=128)
    model = serializers.CharField(max_length=256)
    year = serializers.IntegerField(min_value=1886, max_value=CURRENT_YEAR)
    fuel_type = serializers.ChoiceField(
        choices=Car.FUEL_CHOICES,
        error_messages={
            "invalid_choice": _(
                "Значения «{input}» нет среди допустимых вариантов. Допустимые варианты: "
                + ",".join(map(lambda x: x[0], Car.FUEL_CHOICES))
            )
        },
    )
    transmission = serializers.ChoiceField(
        choices=Car.TRANSMISSION_CHOICES,
        error_messages={
            "invalid_choice": _(
                "Значения «{input}» нет среди допустимых вариантов. Допустимые варианты: "
                + ",".join(map(lambda x: x[0], Car.TRANSMISSION_CHOICES))
            )
        },
    )
    mileage = serializers.IntegerField(min_value=0)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Car
        fields = (
            "id",
            "brand",
            "model",
            "year",
            "fuel_type",
            "transmission",
            "mileage",
            "price",
        )
