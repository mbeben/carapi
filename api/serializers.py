import requests

from django.conf import settings

from rest_framework import serializers
from .models import Car, Rate


class CarSerializer(serializers.ModelSerializer):

    @staticmethod
    def get_url_model_for_make(make):
        url = '{}/vehicles/getmodelsformake/{}?format=json'.format(settings.API_URL, make)
        return url

    def validate(self, attrs):
        request = requests.get(url=self.get_url_model_for_make(attrs['make'])).json()

        # If request returns with Count 0 it means that this Make is invalid
        # Raise a ValidationError since it's invalid
        if not int(request.get('Count')) > 0:
            raise serializers.ValidationError({'make': 'Your make: {} is invalid'.format(attrs['make'])})

        # For loop that checks all results from request and adds its' model name to the results list
        results = []
        for car in request.get('Results'):
            if attrs['model'].lower() in car['Model_Name'].lower():
                results.append(car)

        # If we get no results from this then it means make is valid but there are no valid models for it.
        # Raise a validation error
        if not len(results) > 0:
            raise serializers.ValidationError({
                'model': 'Model: {} is not available for this Make: {}'.format(attrs['model'], attrs['make'])})

        # If we get more than result one, then it means that we need to specify which one we want to add before
        # saving it in database.
        # If model has been specified exactly then we can add it.
        if len(results) > 1:

            # Get exact model variable ready
            exact_model = None
            for result in results:
                if result['Model_Name'].lower() == attrs['model'].lower():
                    exact_model = result['Model_Name']

            # If we do not have exact model but still have multiple cars return validation error.
            if not exact_model:
                raise serializers.ValidationError({
                    'model': 'Model: {} is available in more than one configuration. Please specify. {}'.format(
                        attrs['model'], ", ".join(str(car['Model_Name']) for car in results))
                })

        # Everything is good and we have list with one car in results. return validate
        attrs['make'] = results[0]['Make_Name']
        attrs['model'] = results[0]['Model_Name']

        return super().validate(attrs)

    class Meta:
        model = Car
        fields = '__all__'


class CarListSerializer(serializers.ModelSerializer):

    avg_rating = serializers.IntegerField(source='average_rating')

    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'avg_rating')


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = '__all__'
