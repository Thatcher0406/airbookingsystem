from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Flight, Passenger
from .serializers import FlightSerializer, PassengerSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['flight']
    ordering_fields = ['last_name', 'first_name']
