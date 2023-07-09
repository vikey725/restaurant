from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateTimeField()

class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.SlugField()
