from django.contrib import admin
from . models import AddCustomer, RoomBooking, AddRoom,LoundryBooking, Cleaning

admin.site.register(AddCustomer),
admin.site.register(RoomBooking)
admin.site.register(AddRoom),
admin.site.register(LoundryBooking),
admin.site.register(Cleaning)


