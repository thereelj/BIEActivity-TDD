from django.db import models

# Create your models here.


class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True, editable=False)
    rental = models.CharField(max_length=255)
    checkin = models.DateField(blank=True, null=True)
    checkout = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.rental} Reservation'
