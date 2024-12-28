from django.contrib import admin

from . import models
from .models import CarTechCHar


class CarBrandAdmin(admin.ModelAdmin):
    list_display = ['name']


class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name_model']

class CarTechCHarAdmin(admin.ModelAdmin):
    list_display = ['power', 'color', 'brand', 'model', 'vin', 'year', 'car_milage', 'date_create', 'date_update']
    list_filter = ['power', 'color', 'brand', 'model', 'vin', 'year', 'car_milage', 'date_create', 'date_update']
    search_fields = ['power', 'color', 'brand', 'model', 'vin', 'year', 'car_milage', 'date_create', 'date_update']




admin.site.register(models.CarBrand, CarBrandAdmin)
admin.site.register(models.CarModel, CarModelAdmin)
admin.site.register(models.CarTechCHar, CarTechCHarAdmin)

