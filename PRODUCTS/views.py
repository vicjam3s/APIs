from django.shortcuts import render
from rest_framework import viewsets
from PRODUCTS.serializers import ProductSerializer
from .models import Product
from rest_framework import pagination
from rest_framework import filters
from rest_framework import permissions

# Create your views here.
class ProductPagination(pagination.PageNumberPagination):
    page_size = 5

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'price']
    