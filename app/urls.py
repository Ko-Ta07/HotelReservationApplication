from django.urls import path
from app import views

urlpatterns = [
    path('', views.HotelView.as_view(), name='hotel'),
    path('hotel/<int:pk>/plan/', views.PlanView.as_view(), name='plan'),
    path('calendar/<int:pk>', views.CalendarView.as_view(), name='calendar'),
    path('calendar/<int:pk>/<int:year>/<int:month>/<int:day>', views.CalendarView.as_view(), name='calendar'),
    # path('calendar', views.CalendarView.as_view(), name='calendar'),
    path('booking/<int:plan_id>/', views.BookingView.as_view(), name='booking'),
    path('confirm/', views.BookingView.as_view(), name='confirm'),
    path('thanks', views.ThanksView.as_view(), name='thanks'),
]