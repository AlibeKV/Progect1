from api.django.urls import path
from .views import ProductAPIVew , ProductDetailAPIView

urlpatterns [
    path('product/', ProductAPIVew.as_views(), name='product-list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail')
]