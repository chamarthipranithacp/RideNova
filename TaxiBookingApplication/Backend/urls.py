from django.urls import path
from . import views

urlpatterns = [
    # Customer APIs
    path('customers/add/', views.add_customer, name='add_customer'),
    path('customers/', views.get_customers, name='get_customers'),
    path('customers/update/<int:id>/', views.update_customer, name='update_customer'),
    path('customers/delete/<int:id>/', views.delete_customer, name='delete_customer'),

    # Driver APIs
    path('drivers/add/', views.add_driver, name='add_driver'),
    path('drivers/', views.get_drivers, name='get_drivers'),
    path('drivers/update/<int:id>/', views.update_driver, name='update_driver'),
    path('drivers/delete/<int:id>/', views.delete_driver, name='delete_driver'),

    # Vehicle APIs
    path('vehicles/add/', views.add_vehicle, name='add_vehicle'),
    path('vehicles/', views.get_vehicles, name='get_vehicles'),
    path('vehicles/update/<int:id>/', views.update_vehicle, name='update_vehicle'),
    path('vehicles/delete/<int:id>/', views.delete_vehicle, name='delete_vehicle'),

    # Booking APIs
    path('bookings/add/', views.add_booking, name='add_booking'),
    path('bookings/', views.get_bookings, name='get_bookings'),
    path('bookings/update/<int:id>/', views.update_booking, name='update_booking'),
    path('bookings/delete/<int:id>/', views.delete_booking, name='delete_booking'),

    # Payment APIs
    path('payments/add/', views.add_payment, name='add_payment'),
    path('payments/', views.get_payments, name='get_payments'),
    path('payments/update/<int:id>/', views.update_payment, name='update_payment'),
    path('payments/delete/<int:id>/', views.delete_payment, name='delete_payment'),

    # Admin APIs
    path('admins/add/', views.add_admin, name='add_admin'),
    path('admins/', views.get_admins, name='get_admins'),
    path('admins/update/<int:id>/', views.update_admin, name='update_admin'),
    path('admins/delete/<int:id>/', views.delete_admin, name='delete_admin'),
]
