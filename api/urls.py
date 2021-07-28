from django.urls import path, include

from .viewsets import CarViewSet, RateCreateView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet)


urlpatterns = [
    path('', include(router.urls), ),
    path('rate/', RateCreateView.as_view(), ),
]
