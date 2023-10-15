#from django.shortcuts import generics
#from functools import _PWrapper
from pickle import TRUE
from app.models import (
    Cafe,
    Menu,
    Food
)
from .serializers import (
    CafeSerializer,
    MenuSerializer,
    FoodSerializer
)
from rest_framework import generics, mixins, status , permissions
from rest_framework.response import Response
from api import serializers
#class CafeList(generics.ListAPIView):
#    queryset = Cafe.objects.all()
#    serializer_class = CafeSerializer
#
#class CafeDetail(generics.RerievveAPIView):
#    queryset = Cafe.objects.all()
#    serializer_class = CafeSerializer
#
#class CafePost(generics.CreateAPIView):
#    queryset = Cafe.objects.all()
#    serializer_class = CafeSerializer
#
#class CafePut(generics.UpdateAPIView):
#    queryset = Cafe.objects.all()
#    serializer_class = CafeSerializer
#
#class CafeDelete(generics.DestrroyAPIView):
#    queryset = Cafe.objects.all()
#    serializer_class = CafeSerializer
#-----------------------------------

class CafeAPIView(generics.ListCreateAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

class CafeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer
#
class MenuAPIView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
# Food
class FoodAPIView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
   
class MenuAPI(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView

):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    #def get_permissions(self,):
    #    if self.request.method == 'GET':
    #        return [permissions.AllowAny()]
    #    elif self.request.method == 'POST':
    #        return [permissions.IsAdminUser()]
    #   return []
    def get(self, request , *args, **kwargs):
        menu = self.get_queryset().all()
        serializer = self.get_serializer(menu, many=TRUE)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self , request , *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)


class MenuDetailAPI(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get(self, request , *args, **kwargs):
        return self.retrive(request, *args , **kwargs)
    def put(self, request , *args, **kwargs):
        return self.update(request, *args , **kwargs)
    def delete(self, request , *args, **kwargs):
        return self.destroy(request, *args , **kwargs)
    


class CafeAPI(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView

):
    queryset = Cafe.objects.all()
    serializer_class = MenuSerializer

    #def get_permissions(self,):
    #    if self.request.method == 'GET':
    #        return [permissions.AllowAny()]
    #    elif self.request.method == 'POST':
    #        return [permissions.IsAdminUser()]
    #   return []
    def get(self, request , *args, **kwargs):
        cafe = self.get_queryset().all()
        serializer = self.get_serializer(cafe, many=TRUE)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self , request , *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)


class CafeDetailAPI(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Cafe.objects.all()
    serializer_class = MenuSerializer

    def get(self, request , *args, **kwargs):
        return self.retrive(request, *args , **kwargs)
    def put(self, request , *args, **kwargs):
        return self.update(request, *args , **kwargs)
    def delete(self, request , *args, **kwargs):
        return self.destroy(request, *args , **kwargs)
