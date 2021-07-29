
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Car(models.Model):

    make = models.CharField('Make', max_length=255, )
    model = models.CharField('Model', max_length=255, )

    def __str__(self):
        return '{}: {}'.format(self.make, self.model)

    @property
    def rate_count(self):
        return self.rate_set.count()

    @property
    def average_rating(self):
        rates = self.rate_set.all()
        all_rates = []
        for rate in rates:
            all_rates.append(rate.rate)

        if len(all_rates) == 0:
            return 0

        return round(sum(all_rates)/len(all_rates), 2)


class Rate(models.Model):

    car = models.ForeignKey(Car, verbose_name="car", on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField('Rate', validators=[MinValueValidator(1), MaxValueValidator(5)], 
                                            help_text='Rate for this car.')
