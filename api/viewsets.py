from rest_framework.response import Response

from api.models import Car

from .serializers import CarSerializer, CarListSerializer, RateSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from api_common.viewsets import CreateDestroyModelViewset


class CarViewSet(CreateDestroyModelViewset):
    """
    A simple viewset for viewing, adding and deleting cars.
    """

    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarListView(ListAPIView):
    """
    A simple view for listing all cars
    """
    serializer_class = CarListSerializer
    queryset = Car.objects.all()


class RateCreateView(CreateAPIView):
    """
    A simple view for adding rates.
    """
    serializer_class = RateSerializer


class PopularView(ListAPIView):
    """
    A simple view to list all cars ordered in descending order by amount of rates
    """
