from django.contrib import admin
from .models import Hotel, Staff ,Room, Booking, BookingPlan

admin.site.register(Hotel)
admin.site.register(Staff)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(BookingPlan)