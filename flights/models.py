
from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3, primary_key="")
    city = models.CharField(max_length=64, primary_key="")
    
    def __str__(self):
        return f" {self.city} ({self.code}) "



class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    
    def __str__(self):
        return f" {self.id}: {self.origin} to {self.destination} "

    def is_valid_flight(self):
        return self.origin != self.destination or self.duration >= 0


class Passenger(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    flights = models.ManyToManyField(Flight, related_name="passengers", blank=True)
    
    def __str__(self):
        return f"{self.last} {self.first}"