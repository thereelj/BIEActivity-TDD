from django.urls import path, include

from rental import views

app_name = 'rental'

urlpatterns = [
    path('', views.RentalAPIView.as_view(), name='rental-list'),
    path('<int:id>', views.RentalDetailAPIView.as_view(), name='rental-detail')
]
