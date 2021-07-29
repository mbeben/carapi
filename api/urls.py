from django.urls import path, include

from .views import CarViewSet, RateCreateView, PopularListView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet)


urlpatterns = [
    path('', include(router.urls), name='car'),
    path('rate/', RateCreateView.as_view(), name='rate'),
    path('popular/', PopularListView.as_view(), name='popular')
]
