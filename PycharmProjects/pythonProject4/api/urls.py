from django.urls import path
from .views import CafeAPI, CafeDetailAPI, MenuAPI , MenuDetailAPI

#from .views import (
#    CafeAPIView,
#    CafeDetailAPIView,
#)
#
#
urlpatterns = [
   #path('cafe/list/',CafeAPIView.as_view()),
   #path('cafe/<int:pk>/',CafeDetailAPIView.as_view()),
   path('menu/', MenuAPI.as_view(), name='menu'),
   path('menu/<int:pk>/', MenuDetailAPI.as_view(), name='Menu Detail Api'),
   path('cafe/', CafeAPI.as_view(), name='cafe'),
   path('cafe/<int:pk>/', CafeDetailAPI.as_view(), name='Menu Detail Api'),

]