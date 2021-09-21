from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from .models import Loginmodel
from rest_framework import serializers

class loginserializer(serializers.ModelSerializer):
    class Meta:
        model=Loginmodel
        fields='__all__'

