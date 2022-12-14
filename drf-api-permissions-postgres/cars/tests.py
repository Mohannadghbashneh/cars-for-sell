from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import  status
# Create your tests here.
from django.contrib.auth import get_user_model
from .models import Car

from django.urls import reverse

class CarTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass"
        )
        testuser2.save()

        test_car = Car.objects.create(
            name="bmw",
            seller=testuser1,
            rank=2 ,
            description="test",
            
        )
        test_car.save()


    def setUp(self):
        self.client.login(username='testuser1', password="pass")


    def test_car_model(self):
        car = Car.objects.get(id=1)
        actual_seller = str(car.seller)
        actual_name = str(car.name)
        actual_description = str(car.description)
        actual_rank=2
        self.assertEqual(actual_seller, "testuser1")
        self.assertEqual(actual_name, "bmw")
        self.assertEqual(
            actual_description, "test"
        )
        self.assertEqual(
            actual_rank, 2
        )


    def test_get_car_list(self):
        url = reverse("car_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cars = response.data
        self.assertEqual(len(cars), 1)
        

    def test_auth_required(self):
        self.client.logout()
        url = reverse("car_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_seller_can_delete(self):
        self.client.logout()
        self.client.login(username='testuser2', password="pass")
        url = reverse("car_detail", args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)