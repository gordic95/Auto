from rest_framework import serializers
from .models import CarTechCHar


class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarTechCHar
        fields = '__all__'

    def create(self, validated_data):
        return CarTechCHar.objects.create(**validated_data)


