from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, FormView, View
from django.urls import reverse
from django.urls import reverse_lazy
from datetime import datetime, date, timedelta, time

from app.forms import BookingForm
from .models import Hotel, BookingPlan, Booking

class HotelView(ListView):
    template_name = 'app/hotel.html'
    model = Hotel
    
class PlanView(ListView):
    template_name = 'app/plan.html'
    
    def get_queryset(self):
        return BookingPlan.objects.filter(hotel__pk=self.kwargs['pk'])   
    
    
class CalendarView(View):
    def get(self, request, *args, **kwargs):
        planname_data = BookingPlan.objects.filter(id=self.kwargs['pk']).select_related('hotel')[0]
        today = date.today()
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        
        if year and month and day:
            start_date = date(year=year, month=month, day=day)
        else:
            start_date = today
        days = [start_date + timedelta(days=day) for day in range(7)]
        start_day = days[0]
        end_day = days[-1]
        booking_data = BookingPlan.objects.filter(planname=planname_data)

        target_date = start_date
        calendar_object = MyLocaleHTMLCalendar(locale='ja_jp', pk=self.kwargs['pk'])
        calendar_object.set_pk(self.kwargs['pk'])
        calendar_html = calendar_object.formatmonth(target_date.year, target_date.month)


        return render(request, 'app/calendar.html',{
            'planname_data':planname_data,
            'plan_id': self.kwargs['pk'],
            'calendar': calendar,
            'days': days,
            'start_day': start_day,
            'end_day': end_day,
            'before': days[0] - timedelta(days=7),
            'next': days[-1] + timedelta(days=1),
            'today': today,
            'target_date': target_date,
            'previous_month': (target_date.replace(day=1) - timedelta(days=1)).month,
            'next_month': (target_date.replace(day=1) + timedelta(days=31)).month,
            'calendar_html': calendar_html,
        })        
        
import calendar
class MyLocaleHTMLCalendar(calendar.LocaleHTMLCalendar):
    cssclass_month = 'table table-bordered bg-light'
    theyear = 0
    themonth = 0

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk')
        super().__init__(*args, **kwargs)
        self.setfirstweekday(calendar.SUNDAY)

    def set_pk(self, pk):
        self.pk = pk

    def formatmonth(self, theyear, themonth, withyear=True):
        self.theyear = theyear
        self.themonth = themonth
        return super().formatmonth(theyear, themonth, withyear)


    def formatday(self, day, weekday):
        """
        Return a day as a table cell.
        """
        if day == 0:
            # day outside month
            return '<td class="%s">&nbsp;</td>' % self.cssclass_noday
        else:
            #url = reverse('booking', kwargs={'pk': self.pk, 'year': self.theyear, 'month': self.themonth, 'day': day})
            url = reverse('booking', kwargs={'plan_id': self.pk})
            # return '<td class="%s"><a href="%s">%d</a></td>' % (self.cssclasses[weekday], url, day)
            return f'<td class="{self.cssclasses[weekday]}"><a href="{url}">{day}</a></td>'

    
class BookingView(FormView):
    template_name = 'app/booking.html'
    form_class = BookingForm
    success_url = reverse_lazy('thanks')
    
    def get_template_names(self):
        if self.request.POST.get('step') == 'confirm' and self.get_form().is_valid():
            return ['app/confirm.html']  # return先は合っていますか？
        else:
            return ['app/booking.html']  # return先は合っていますか？
        
        
    def form_valid(self, form):
        if self.request.POST['step'] != 'thanks':  # ここでエラーになって落ちてしまいます..
            return self.render_to_response(self.get_context_data(form=form))
        
        data = form.cleaned_data
        obj = Booking(**data)
        obj.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plan_id = self.kwargs.get('plan_id')
        print(plan_id)
        context['plan'] = BookingPlan.objects.get(pk=plan_id)
        return context

    
class ThanksView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/thanks.html')    