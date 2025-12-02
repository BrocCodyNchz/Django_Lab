from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import locationSerializer
from .models import location

class LocationList(generics.ListCreateAPIView):
    queryset = location.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = locationSerializer # tell django what serializer to use
class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = location.objects.all().order_by('id')
    serializer_class = locationSerializer