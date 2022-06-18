from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Hotel, BookingPlan


#class HotelView(View):
    #def get(self, request, *args, **kwargs):
        #hotel_data = Hotel.objects.all()
        
        #return render(request, 'app/hotel.html', {
           # 'hotel_data':hotel_data
        #})
        
class HotelView(ListView):
    template_name = 'app/hotel.html'
    model = Hotel
    
class PlanView(ListView):
    template_name = 'app/plan.html'
    model = BookingPlan
        