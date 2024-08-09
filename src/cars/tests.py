import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Car


@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser", password="testpass")


@pytest.fixture
def api_client(user):
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return client


@pytest.fixture
def car(db):
    return Car.objects.create(
        brand="Toyota",
        model="Camry",
        year=2020,
        fuel_type="бензин",
        transmission="автоматическая",
        mileage=10000,
        price="25000.00",
    )


class TestCarService:
    """Тесты для api cars"""

    def test_create_car(self, api_client):
        car_data = {
            "brand": "Toyota",
            "model": "Camry",
            "year": 2020,
            "fuel_type": "бензин",
            "transmission": "автоматическая",
            "mileage": 10000,
            "price": "25000.00",
        }
        url = reverse("cars-list")
        response = api_client.post(url, car_data, format="json")
        assert response.status_code == 201
        assert response.data["brand"] == car_data["brand"]

    def test_list_cars(self, api_client, car):
        url = reverse("cars-list")
        response = api_client.get(url)
        assert response.status_code == 200
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["brand"] == car.brand

    def test_retrieve_car(self, api_client, car):
        url = reverse("cars-detail", kwargs={"pk": car.id})
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data["brand"] == car.brand

    def test_update_car(self, api_client, car):
        updated_data = {
            "brand": "Toyota",
            "model": "Camry",
            "year": 2021,
            "fuel_type": "бензин",
            "transmission": "автоматическая",
            "mileage": 12000,
            "price": "27000.00",
        }
        url = reverse("cars-detail", kwargs={"pk": car.id})
        response = api_client.put(url, updated_data, format="json")
        assert response.status_code == 200
        assert response.data["year"] == updated_data["year"]
        assert response.data["mileage"] == updated_data["mileage"]

    def test_delete_car(self, api_client, car):
        url = reverse("cars-detail", kwargs={"pk": car.id})
        response = api_client.delete(url)
        assert response.status_code == 204
        assert not Car.objects.filter(id=car.id).exists()

    def test_unauthorized_access(self, api_client, car):
        api_client.credentials()  # Сброс токена аутентификации
        url = reverse("cars-list")
        response = api_client.get(url)
        assert response.status_code == 401
