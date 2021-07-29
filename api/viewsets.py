from django.db.models import Count

from api.models import Car

from .serializers import CarSerializer, CarListSerializer, RateSerializer, PopularSerializer
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

    def get_serializer_class(self):
        if self.action == 'list':
            self.serializer_class = CarListSerializer
        return super().get_serializer_class()


class RateCreateView(CreateAPIView):
    """
    A simple view for adding rates.
    """
    serializer_class = RateSerializer


class PopularListView(ListAPIView):
    """
    A simple view to list all cars ordered in descending order by amount of rates
    """
    serializer_class = PopularSerializer
    queryset = Car.objects.all().annotate(num_rates=Count('rate')).order_by('-num_rates')
