from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator
from django.db import models


class CarBrand(models.Model):
    name = models.CharField(max_length=50, verbose_name='Марка')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

class CarModel(models.Model):
    name_model = models.CharField(max_length=50, verbose_name='Модель')


    def __str__(self):
        return self.name_model

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

class CarTechCHar(models.Model):
    power = models.PositiveIntegerField(validators=[MaxValueValidator(2000)], verbose_name='Мощность')
    color = models.CharField(max_length=10, verbose_name='Цвет')
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, verbose_name='Марка')
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name='Модель')
    vin = models.CharField(unique=True, max_length=17, verbose_name='VIN')
    year = models.PositiveIntegerField(validators=[MinValueValidator(1800)], verbose_name='Год')
    car_milage = models.PositiveIntegerField(validators=[MaxValueValidator(600000)], verbose_name='Пробег')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.brand} {self.model}'

    class Meta:
        verbose_name = 'Технические характеристики'
        verbose_name_plural = 'Технические характеристики'


