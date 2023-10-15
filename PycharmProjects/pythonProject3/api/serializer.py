from dataclasses import field
from unittest import mock
from rest_framework import serializers
from app.models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
        )