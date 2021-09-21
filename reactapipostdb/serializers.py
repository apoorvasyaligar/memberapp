from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import infomodel



class infoserializer(serializers.ModelSerializer):
    class Meta:
        model=infomodel
        fields='__all__'