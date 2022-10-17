from django.test import TestCase, Client
from .models import Airport, Flight, Passenger
from django.db.models import Max

# Create your tests here.
class FlightTestCase(TestCase):
    def setUp(self):
        # Create Airports
        a1 = Airport.objects.create(code='AAA', city='City A')
        a2 = Airport.objects.create(code='BBB', city='City B')
        
        # create Flights
        Flight.objects.create(origin=a1, destination=a2, duration=100)
        Flight.objects.create(origin=a1, destination=a1, duration=100)
        Flight.objects.create(origin=a1, destination=a2, duration=100)
        
    def test_departure_count(self):
        a = Airport.objects.get(code='AAA')
        self.assertEqual(a.departures.count(), 3)
    
    def test_arrivals_count(self):
        a = Airport.objects.get(code='BBB')
        self.assertEqual(a.arrivals.count(), 2)
    
    def test_valid_flight(self):
        a1 = Airport.objects.create(code='AAA', city='City A')
        a2 = Airport.objects.create(code='BBB', city='City B')
        f = Flight.objects.create(origin=a1, destination=a2, duration=100)
        self.assertTrue(f.is_valid_flight())
        
        
    def test_invalid_flight_destination(self):
        a1 = Airport.objects.create(code='AAA', city='City A')
        a2 = Airport.objects.create(code='BBB', city='City B')
        f = Flight.objects.create(origin=a1, destination=a1, duration=100)
        self.assertFalse(f.is_valid_flight())
        
    def test_invalid_flight_duration(self):
        a1 = Airport.objects.create(code='AAA', city='City A')
        a2 = Airport.objects.create(code='BBB', city='City B')
        f = Flight.objects.create(origin=a1, destination=a2, duration=-100)
        self.assertFalse(f.is_valid_flight())
        
    def test_index(self):
        c = Client()
        response = c.get("/flights/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['flights'].count(), 3)
        
    def test_valid_flight_page(self):
        a1 = Airport.objects.get(code="AAA")
        f = Flight.objects.get(origin=a1, destination=a1)
        c = Client()
        response = c.get(f"/flights/{f.id}")
        self.assertEqual(response.status_code, 200)
        
    def test_invalid_flight_page(self):
        max_id = Flight.objects.all().aggregate(Max('id'))["id__max"]
        a1 = Airport.objects.get(code="AAA")
        f = Flight.objects.get(origin=a1, destination=a1)
        c = Client()
        response = c.get(f"/flights/{max_id + 1}")
        self.assertEqual(response.status_code, 404)
        
    def test_flight_page_passengers(self):
        f = Flight.objects.get(pk=1)
        p = Passenger.objects.create(first="Amza", last="Omiteru")
        f.passengers.add(p)
        
        c = Client()
        response = c.get(f'/flights/{f.id}')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['passengers'].count(), 1)
        
        
    def test_flight_page_non_passengers(self):
        f = Flight.objects.get(pk=1)
        p = Passenger.objects.create(first="Amza", last="Omiteru")
        
        c = Client()
        response = c.get(f'/flights/{f.id}')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['non_passengers'].count(), 1)