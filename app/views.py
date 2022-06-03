from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Hotel, Staff


class HotelView(View):
    def get(self, request, *args, **kwargs):
        hotel_data = Hotel.objects.all()
        
        return render(request, 'app/hotel.html', {
            'hotel_data':hotel_data
        })
        

class StaffView(View):
    def get(self, request, *args, **kwargs):
        hotel_data = get_object_or_404(Hotel, id=self.kwargs['pk'])
        staff_data = Staff.objects.filter(hotel=hotel_data).select_related('user')
        
        return render(request, 'app/staff.html',{
            'hotel_data':hotel_data,
            'staff_data': staff_data
        })       