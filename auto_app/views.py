from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from yaml import serialize

from .models import CarTechCHar, CarBrand, CarModel
from rest_framework import generics, status
from .serializers import AutoSerializer, AutoCreateSerializer


class AutoList(generics.ListAPIView):
    queryset = CarTechCHar.objects.all()
    serializer_class = AutoSerializer


class AutoDetailVin(generics.RetrieveAPIView):
    queryset = CarTechCHar.objects.all()
    serializer_class = AutoSerializer
    def get(self, request, vin):
        car = CarTechCHar.objects.get(vin=vin)
        serializer = AutoSerializer(car)
        return Response(serializer.data)

#Представление для создания авто по всем характеристика + выбор Бренда и Модели
# class CreateAuto(generics.CreateAPIView):
#     queryset = CarTechCHar.objects.all()
#     serializer_class = AutoSerializer


#Представление для создания авто по характеристика Бренд и Модель
# class CreateAuto(generics.CreateAPIView):
#     queryset = CarTechCHar.objects.all()
#     serializer_class = AutoCreateSerializer


#Предаставление для создания авто с собственным написанием бренда
class CreateAuto(generics.CreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = AutoCreateSerializer

    #Нужно как то создать серилизатор для модели и бренда и засунуть его в представление





