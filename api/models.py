from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator


class Car(models.Model):

    make = models.CharField('Make', max_length=255, )
    model = models.CharField('Model', max_length=255, )

    def __str__(self):
        return '{}: {}'.format(self.make, self.model)

    @property
    def rates(self):
        return ''


class Rate(models.Model):

    car = models.ForeignKey(Car, verbose_name="car", on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField('Rate', validators=[MinValueValidator(1), MaxValueValidator(5)], 
                                            help_text='Rate for this car.')
