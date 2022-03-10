from django.shortcuts import render
from rest_framework import viewsets
from . models import Sex, PetInfo
from . serializers import SexSerializer, PetInfoSerializer

# Create your views here.

# SexViewSet define the view behavior of the sex endpoint.
class SexViewSet(viewsets.ModelViewSet):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer


# PetInfoViewSet define the view behavior of the PetInfo endpoint.
class PetInfoViewSet(viewsets.ModelViewSet):
    queryset = PetInfo.objects.all()
    serializer_class = PetInfoSerializer
    


