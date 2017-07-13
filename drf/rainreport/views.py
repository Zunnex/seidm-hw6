# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from rainreport.models import Rainfall, Station
from rainreport.serializers import RainfallSerializer, StationSerializer
from rest_framework import generics

class RainfallList(generics.ListCreateAPIView):
    queryset = Rainfall.objects.all()
    serializer_class = RainfallSerializer

class RainfallDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rainfall.objects.all()
    serializer_class = RainfallSerializer

class StationList(generics.ListCreateAPIView):
    queryset = Station.objects.filter(county='基隆市')
    serializer_class = StationSerializer

