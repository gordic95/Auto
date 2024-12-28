from rest_framework import serializers
from .models import CarTechCHar, CarBrand, CarModel


class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarTechCHar
        fields = '__all__'

#Серилизатор для технических характеристик
# class AutoCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CarTechCHar
#         fields = 'model', 'brand'
#
#     def create(self, validated_data):
#         return CarTechCHar.objects.create(**validated_data)

class AutoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'

    def create(self, validated_data):
        return CarBrand.objects.create(**validated_data)
