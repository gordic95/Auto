from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CarTechCHar, CarBrand, CarModel
from rest_framework import generics, status
from .serializers import AutoSerializer


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


class CreateAuto(generics.CreateAPIView):
    queryset = CarTechCHar.objects.all()
    serializer_class = AutoSerializer




