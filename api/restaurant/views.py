from django.shortcuts import render
from rest_framework import viewsets
#from .models import Note
from .serializers import NoteSerializer
from .models import Restaurant, MenuItem, Note
from .serializers import RestaurantSerializer, MenuItemSerializer, NoteSerializer

# Create your views here.
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer