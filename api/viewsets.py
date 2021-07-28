from rest_framework import status
from rest_framework.response import Response

from api.models import Car

from .serializers import CarSerializer, RateSerializer
from rest_framework.generics import CreateAPIView
from api_common.viewsets import CreateListDestroyModelViewset


class CarViewSet(CreateListDestroyModelViewset):
    """
    A simple viewset for viewing, adding and deleting cars.
    """

    serializer_class = CarSerializer
    queryset = Car.objects.all()


class RateCreateView(CreateAPIView):
    """
    A simple view for adding rates.
    """
    serializer_class = RateSerializer
