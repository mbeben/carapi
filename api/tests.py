from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Car, Rate


class CarTests(APITestCase):

    def __init__(self, methodname: str = ...) -> None:
        super().__init__(methodname)

        self.car1 = {'make': 'Ford', 'model': 'Focus'}
        self.car2 = {'make': 'Hyundai', 'model': 'Ioniq'}

    def setUp(self) -> None:
        car1 = Car.objects.create(make=self.car1['make'], model=self.car1['model'])
        car2 = Car.objects.create(make=self.car2['make'], model=self.car2['model'])

        # Create 6 rates for car1 and 5 rates car2
        i = 0
        while i < 6:
            Rate.objects.create(car=car1, rate=5)
            if not i == 0:
                Rate.objects.create(car=car2, rate=4)
            i += 1

    def test_cars_get(self):
        # Test if getting cars results in HTTP 200
        url = reverse('car-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        rj = response.json()
        # Test if first car is Ford focus
        self.assertEqual(rj[0]['make'], self.car1['make'])
        self.assertEqual(rj[0]['model'], self.car1['model'])

        # Test if second car is Hyundai Ioniq
        self.assertEqual(rj[1]['make'], self.car2['make'])
        self.assertEqual(rj[1]['model'], self.car2['model'])

        # Test if first car has avg rating of 5 and second avg rating of 4
        self.assertEqual(rj[0]['avg_rating'], 5)
        self.assertEqual(rj[1]['avg_rating'], 4)

    def test_cars_create(self):
        # Test if adding a car results in HTTP 201
        url = reverse('car-list')
        data = {'make': 'Ford', 'model': 'Focus'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Test if make and model for the car was added successfully
        self.assertEqual(Car.objects.first().make.lower(), data['make'].lower())
        self.assertEqual(Car.objects.first().model.lower(), data['model'].lower())

    def test_cars_remove(self):
        # Test if request with non-existing pk will return HTTP 404
        url = reverse('car-detail', kwargs={'pk': 9001})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Test if removing an object from database returns HTTP 204
        car3 = Car.objects.create(make='BMT', model='125i')
        url = reverse('car-detail', kwargs={'pk': car3.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_rate_post(self):
        url = reverse('rate')
        car4 = Car.objects.create(make='FIAT', model='124 Spider')
        data = {'rate': 5, 'car_id': car4.pk}
        response = self.client.post(url, data, format='json')

        # Assert if rate was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert if rate count for this car instance is exactly 1
        self.assertEqual(car4.rate_set.count(), 1)

    def test_popular(self):
        url = reverse('popular')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        rj = response.json()
        # Test if first car is Ford focus
        self.assertEqual(rj[0]['make'], self.car1['make'])
        self.assertEqual(rj[0]['model'], self.car1['model'])

        # Test if second car is Hyundai Ioniq
        self.assertEqual(rj[1]['make'], self.car2['make'])
        self.assertEqual(rj[1]['model'], self.car2['model'])

        # Test if first car has rate count of 6 and second avg rating of 5
        self.assertEqual(rj[0]['rate_count'], 6)
        self.assertEqual(rj[1]['rate_count'], 5)
