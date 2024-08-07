from rest_framework import serializers
from .models import Person

class PeopleSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = '__all__'