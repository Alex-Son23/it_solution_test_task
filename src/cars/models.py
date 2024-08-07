from django.db import models


class Car(models.Model):
    """
    Модель машины, со следующими полями:
        Марка
        Модель
        Год выпуска
        Тип топлива (бензин, дизель, электричество, гибрид)
        Тип КПП (механическая, автоматическая, вариатор, робот)
        Пробег
        Цена
    """

    FUEL_CHOICES = [
        ("бензин", "Бензин"),
        ("дизель", "Дизель"),
        ("электричество", "Электричество"),
        ("гибрид", "Гибрид"),
    ]

    TRANSMISSION_CHOICES = [
        ("механическая", "Механическая"),
        ("автоматическая", "Автоматическая"),
        ("вариатор", "Вариатор"),
        ("робот", "Робот"),
    ]

    brand = models.CharField(verbose_name="Марка машины", max_length=128)
    model = models.CharField(verbose_name="Модель машины", max_length=256)
    year = models.PositiveSmallIntegerField(verbose_name="Год выпуска")
    fuel_type = models.CharField(
        max_length=16,
        choices=FUEL_CHOICES,
    )
    transmission = models.CharField(
        max_length=16,
        choices=TRANSMISSION_CHOICES,
    )
    mileage = models.PositiveIntegerField(verbose_name="Пробег")
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Цена")
