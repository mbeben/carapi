from api.models import Car

from .serializers import CarSerializer, RateSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from api_common.viewsets import CreateListDestroyModelViewset


class CarViewSet(CreateListDestroyModelViewset):
    """
    A simple viewset for viewing, adding and deleting cars.
    """

    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RateCreateView(CreateAPIView):
    """
    A simple view for adding rates.
    """
    serializer_class = RateSerializer


class PopularView(ListAPIView):
    """
    A simple view to list all cars ordered in descending order by amount of rates
    """
