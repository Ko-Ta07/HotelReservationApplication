from django.urls import path
from sample_confirm_view import views

app_name = 'sample_confirm_view'

urlpatterns = [
    path('sample1/', views.Sample1View.as_view(), name='sample1'),
    path('sample1/complete/', views.Sample1CompleteView.as_view(), name='sample1_complete'),

    path('sample2/', views.Sample2View.as_view(views.Sample2View.FORMS), name='sample2'),
    path('sample2/complete/', views.Sample2CompleteView.as_view(), name='sample2_complete'),
]