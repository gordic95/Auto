from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class CarBrand(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

class CarModel(models.Model):
    name_model = models.CharField(max_length=50)


    def __str__(self):
        return self.name_model

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

class CarTechCHar(models.Model):
    power = models.PositiveIntegerField(validators=[MaxValueValidator(2000)])
    color = models.CharField(max_length=50)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    vin = models.IntegerField(unique=True)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1800)])
    car_milage = models.PositiveIntegerField(validators=[MaxValueValidator(600000)])



    def __str__(self):
        return f'{self.brand} {self.model}'

    class Meta:
        verbose_name = 'Технические характеристики'
        verbose_name_plural = 'Технические характеристики'
