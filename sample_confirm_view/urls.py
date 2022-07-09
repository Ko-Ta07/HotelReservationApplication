from django.urls import path
from sample_confirm_view import views

app_name = 'sample_confirm_view'

urlpatterns = [
    path('sample1/', views.Sample1View.as_view(), name='sample1'),
    path('sample1/complete/', views.Sample1CompleteView.as_view(), name='sample1_complete'),
]