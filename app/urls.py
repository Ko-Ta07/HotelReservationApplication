from django.urls import path
from app import views

urlpatterns = [
    path('', views.HotelView.as_view(), name='hotel'),
]