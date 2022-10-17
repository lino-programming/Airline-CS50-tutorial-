from django.shortcuts import render
from django.shortcuts import HttpResponse,HttpResponseRedirect,reverse, Http404
from .models import *

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })
    
def flight(request, flight_id):
    try:
        flight = Flight.objects.get(id=flight_id)
        return render(request, "flights/flight.html", {
            "flight": flight,       
            "passengers": flight.passengers.all(),
            "non_passengers": Passenger.objects.exclude(flights=flight).all(),
        
        })
    except:
        raise Http404("Flight does not exist")

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(id=flight_id)
        passenger = Passenger.objects.get(id=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flights:flight", args=(flight.id,)))