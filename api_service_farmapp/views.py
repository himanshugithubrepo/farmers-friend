from django.shortcuts import render
from rest_framework import generics
from .serializers import FarmerDetailsSerializer
from .models import FarmerDetails

# Create your views here.
class RegisterFarmer(generics.ListCreateAPIView):
    queryset = FarmerDetails.objects.all()
    serializer_class = FarmerDetailsSerializer
