import email
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from app.forms import BookingForm
from .models import Hotel, BookingPlan, Booking


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
    
    def get_queryset(self):
        return BookingPlan.objects.filter(hotel__pk=self.kwargs['pk'])   
    
class BookingView(FormView):
    template_name = 'app/booking.html'
    form_class = BookingForm
    success_url = reverse_lazy('hotel')
    
    def form_valid(self, form):
        stayplan = form.cleaned_data['stayplan']
        checkindate = form.cleaned_data['checkindate']
        stay = form.cleaned_data['stay']
        checkintime = form.cleaned_data['checkintime']
        number_of_rooms = form.cleaned_data['number_of_rooms']
        number_of_guests = form.cleaned_data['number_of_guests']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        first_name_kana = form.cleaned_data['first_name_kana']
        last_name_kana = form.cleaned_data['last_name_kana']
        post = form.cleaned_data['post']
        prefecture = form.cleaned_data['prefecture']
        address = form.cleaned_data['address']
        tel = form.cleaned_data['tel']
        age = form.cleaned_data['age']
        email = form.cleaned_data['email']
        remarks = form.cleaned_data['remarks']
        loginuser = form.cleaned_data['loginuser']
        Booking.objects.create(
            stayplan=stayplan,
            checkindate=checkindate,
            stay=stay,
            checkintime=checkintime,
            number_of_rooms=number_of_rooms,
            number_of_guests=number_of_guests,
            first_name=first_name,
            last_name=last_name,
            first_name_kana=first_name_kana,
            last_name_kana=last_name_kana,
            post=post,
            prefecture=prefecture,
            address=address,
            tel=tel,
            age=age,
            email=email,
            remarks=remarks,
            loginuser=loginuser,
        )
        return super().form_valid(form)