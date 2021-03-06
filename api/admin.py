from django.contrib import admin

from .models import Car, Rate


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    list_display = ('make', 'model')

    class Meta:
        model = Car


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):

    list_display = ('car', 'rate')

    class Meta:
        model = Rate
