from django.urls import path, include

from rental import views

app_name = 'rental'

urlpatterns = [
    path('rentals/', views.RentalAPIView.as_view(), name='rental-list'),
    path('rental/<int:rental_id>', views.RentalDetailAPIView.as_view(), name='rental-detail'),
    path('rental/reservations/', views.ReservationAPIView.as_view(), name='reservation-list'),
    path('rental/reservation/<int:reservation_id>',
         views.ReservationDetailAPIView.as_view(), name='reservation-detail')
]
