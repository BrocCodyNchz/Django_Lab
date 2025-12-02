from rest_framework import serializers 
from .models import location 

class LocationSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = location # tell django which model to use
        fields = ('id', 'street', 'city', 'state',) #