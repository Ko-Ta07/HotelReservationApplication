from dataclasses import fields
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['stayplan', 'checkindate', 'stay', 'checkintime', 'number_of_rooms', 'number_of_guests',
                  'first_name', 'last_name', 'first_name_kana', 'last_name_kana', 'post', 'prefecture', 
                  'address', 'tel', 'age', 'email', 'remarks', 'loginuser',]
        
        def __init__(self, *args, **kwargs):
            for field in self.base_fields.values():
                field.widget.attrs.update({"class":"form-control"})
                super().__init__(*args, **kwargs)