from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Hotel


class HotelView(View):
    def get(self, request, *args, **kwargs):
        hotel_data = Hotel.objects.all()
        
        return render(request, 'app/hotel.html', {
            'hotel_data':hotel_data
        })
        