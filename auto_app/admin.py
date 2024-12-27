from django.contrib import admin

from . import models

class CarBrandAdmin(admin.ModelAdmin):
    list_display = ['name']

class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name_model']

class CarTechCHarAdmin(admin.ModelAdmin):
    list_display = ['power', 'color', 'brand', 'model', 'vin', 'year', 'car_milage']
    list_filter = ['power', 'color', 'brand', 'model', 'vin', 'year', 'car_milage']
    search_fields = ['power', 'color', 'brand', 'model', 'vin', 'year', 'car_milage']




admin.site.register(models.CarBrand, CarBrandAdmin)
admin.site.register(models.CarModel, CarModelAdmin)
admin.site.register(models.CarTechCHar, CarTechCHarAdmin)

