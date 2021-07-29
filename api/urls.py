from django.urls import path, include

from .viewsets import CarViewSet, RateCreateView, PopularListView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet)


urlpatterns = [
    path('', include(router.urls), ),
    path('rate/', RateCreateView.as_view(), ),
    path('popular/', PopularListView.as_view(), )
]
