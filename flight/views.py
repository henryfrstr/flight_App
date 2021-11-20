from .models import Flight, Reservation
from .serializers import FlightSerializer, ReservationSerializer, StaffFlightSerializer
from rest_framework import serializers, viewsets, filters
from .permissions import IsStuffOrReadOnly


class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = StaffFlightSerializer
    permission_classes = (IsStuffOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('departureCity', 'arrivalCity', 'dateOfDepature')

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return super().get_serializer_class()
        else:
            return FlightSerializer

    def get_queryset(self):


class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()  # Reservation.objects.all(), self.queryset
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)
