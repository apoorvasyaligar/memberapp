from django.db import models
from django.shortcuts import render
from .models import infomodel
from .serializers import infoserializer
from rest_framework import viewsets
# Create your views here.

class infoviewset(viewsets.ModelViewSet):
    queryset=infomodel.objects.all()
    serializer_class=infoserializer
