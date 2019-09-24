from django.shortcuts import render
from .models import Food
from .serializers import FoodSerializer
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
# Create your views here.
