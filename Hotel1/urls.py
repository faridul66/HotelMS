from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('main/', views.after, name='main'),
    path('AddCustomer/', views.add, name='AddCustomer'),
    path('add_submission/', views.add_submission, name='add_submission'),
    path('add_customer_report/', views.customer_report, name='add_customer_report'),
    path('add_room/', views.add_room, name='add_room'),
    path('add_room_submission/', views.add_room_submission, name='add_room_submission'),
    path('add_room_report/', views.add_room_report, name='add_room_report'),
    path('add_room_booking/', views.add_room_booking, name='add_room_booking'),
    path('add_room_booking_submission/', views.add_room_booking_submission, name='add_room_booking_submission'),
    path('add_room_booking_report/', views.add_room_booking_report, name='add_room_booking_report'),
    path('add_room_billing/', views.add_room_billing, name='add_room_billing'),
    path('room_billing_report/', views.room_billing_report, name='room_billing_report'),
    path('room_billing_submission/', views.room_billing_submission, name='room_billing_submission'),
    path('add_cleaning/', views.add_cleaning, name='add_cleaning'),
    path('add_cleaning_report/', views.add_cleaning_report, name='add_cleaning_report'),
    path('add_cleaning_submission/', views.add_cleaning_submission, name='add_cleaning_submission'),
    path('add_loundry/', views.add_loundry, name='add_loundry'),
    path('loundry_submission/', views.loundry_submission, name='loundry_submission'),
    path('add_loundry_report/', views.add_loundry_report, name='add_loundry_report')



]
