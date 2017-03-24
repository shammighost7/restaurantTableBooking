from django.shortcuts import render_to_response
from rest_framework import viewsets
from rest_framework import filters

from reservations.models import Reservation
from reservations.serializers import ReservationSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_fields = ('customer')
