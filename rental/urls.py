from django.urls import path, include

from rental import views

app_name = 'rental'

urlpatterns = [
    path('rentals', views.RentalAPIView.as_view(), name='rental-list')
]
