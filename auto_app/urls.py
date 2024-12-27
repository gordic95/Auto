from django.urls import path

from .views import AutoList, AutoDetailVin, CreateAuto



urlpatterns = [
    path('auto_list/', AutoList.as_view(), name='auto_list'),
    path('auto_detail/<str:vin>/', AutoDetailVin.as_view(), name='auto_detail_vin'),
    path('auto_create/', CreateAuto.as_view(), name='auto_create'),
]