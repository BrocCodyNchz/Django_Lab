from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import locationsSerializer
from .models import locations

class LocationsList(generics.ListCreateAPIView):
    queryset = locations.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = locationsSerializer # tell django what serializer to use
class LocationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = locations.objects.all().order_by('id')
    serializer_class = locationsSerializer