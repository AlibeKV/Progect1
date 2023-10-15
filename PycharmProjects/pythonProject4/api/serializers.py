from dataclasses import field
from xml.parsers.expat import model
from rest_framework import serializers
from app.models import (
    Cafe,
    Menu,
    Food
)
class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
    
