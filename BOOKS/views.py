from django.shortcuts import render
from rest_framework import viewsets
from BOOKS.serializers import BookSerializer
from .models import *

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer