from django.urls import path
from sample_confirm_view import views

app_name = 'sample_confirm_view'

urlpatterns = [
    path('sample1/', views.Sample1View.as_view(), name='sample1'),
    path('sample1/complete/', views.Sample1CompleteView.as_view(), name='sample1_complete'),

    path('sample2/', views.Sample2View.as_view(views.Sample2View.FORMS), name='sample2'),
    path('sample2/complete/', views.Sample2CompleteView.as_view(), name='sample2_complete'),

    path('sample3/', views.Sample3View.as_view(), name='sample3'),
    path('sample3/form-valid/', views.Sample3FormValidView.as_view(), name='sample3_form_valid'),
    path('sample3/complete/', views.Sample3CompleteView.as_view(), name='sample3_complete'),
]