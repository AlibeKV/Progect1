from django.shortcuts import render
from rest_framework import generics
from .serializer import ProductSerializer
from app.models import Product

class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer