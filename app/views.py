import email
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, FormView, View
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
    success_url = reverse_lazy('thanks')
    
    def get_template_names(self):
        if self.request.POST.get('step') == 'confirm' and self.get_form().is_valid():
            return['app/confirm.html']  # return先は合っていますか？
        else:
            return['app/booking.html']  # return先は合っていますか？
        
        
    def form_valid(self, form):
        if self.request.POST['step'] != 'thanks':  # ここでエラーになって落ちてしまいます..
            return self.render_to_response(self.get_context_data(form=form))
        
        data = form.cleaned_data
        obj = Booking(**data)
        obj.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plan_id = self.request.GET.get('plan_id')
        print(plan_id)
        context['plan'] = BookingPlan.objects.get(pk=plan_id)
        return context

    
class ThanksView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/thanks.html')    